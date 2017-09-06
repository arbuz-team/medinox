from server.manage.switch.website.base import *
from server.ground.product.models import *


class Product_Content:

    def Get_Product_Descriptions(self):
        result = ''

        for description in SQL.Filter(
                Model_Description, product=self.product):

            result += description.header
            result += description.paragraph

        return result.lower()

    def Calculate_Priority(self, word):
        word = word.lower()
        accuracy = 0

        accuracy += self.name.count(word) * 10
        accuracy += self.brand.count(word) * 3
        accuracy += self.description.count(word)

        return accuracy

    def __init__(self, product):

        self.product = product
        self.name = product.name.lower()
        self.brand = product.brand.name.lower()
        self.description = self.Get_Product_Descriptions()



class Sort_List:

    def Generate_Priority_List(self):
        priority_list = []

        for element in self.sort_list:

            # create vars
            product_id = element[0]
            content = element[1]
            priority = 0

            # calculate priority for all words
            for word in self.words:
                priority += content.Calculate_Priority(word)

            # create list element
            priority_list.append((priority, product_id))

        return priority_list

    def Create_List(self):

        for product in self.products:

            element = (
                product.pk, # repetitions set range
                Product_Content(product)
            )

            self.sort_list.append(element)

    def __init__(self, products, words):

        self.sort_list = []
        self.products = products
        self.words = words
        self.Create_List()



class Sort_By_Accuracy(Base):

    def __Get_Sorted_Products(self, sorted_priority_list):

        # get index column from priority list
        index_list = [e[1] for e in sorted_priority_list]
        sorting = ''

        # create sorting extra query
        for index_to, index_from in enumerate(index_list):
            sorting += 'WHEN id={0} THEN {1} '.format(index_from, index_to)

        sorting = 'CASE {0} END'.format(sorting)

        # get sorted product from database
        return SQL.Filter(Model_Product, pk__in=self.products).extra(
            select={'sorting': sorting}, order_by=['sorting'])

    def Sort(self):

        # have no words
        if not self.words:
            return self.products

        # have no products
        if not self.products:
            return self.products

        # generate priority list
        sort_list = Sort_List(self.products, self.words)
        priority_list = sort_list.Generate_Priority_List()

        # sort products
        direction = self.request.session['searcher_sort_direction']
        if direction == 'descending': priority_list.sort(reverse=True)
        if direction == 'ascending': priority_list.sort()

        # select sorted products from database
        return self.__Get_Sorted_Products(priority_list)

    def __init__(self, search_engine):
        Base.__init__(self, search_engine)
        self.products = search_engine.products
        self.words = search_engine.words

