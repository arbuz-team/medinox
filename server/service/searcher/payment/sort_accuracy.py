from server.manage.switch.website.base import *
from server.service.payment.models import *


class Payment_Content:

    def Calculate_Priority(self, word):
        word = word.lower()
        accuracy = 0

        accuracy += self.user.email.count(word) * 10
        accuracy += self.user.username.count(word) * 8
        accuracy += self.delivery_address.name.count(word) * 5
        accuracy += self.delivery_address.surname.count(word) * 5
        accuracy += self.delivery_address.company_name.count(word) * 5
        accuracy += self.delivery_address.nip.count(word) * 5
        accuracy += self.invoice_address.name.count(word) * 5
        accuracy += self.invoice_address.surname.count(word) * 5
        accuracy += self.invoice_address.company_name.count(word) * 5
        accuracy += self.invoice_address.nip.count(word) * 5

        return accuracy

    def __init__(self, payment):

        self.payment = payment
        self.user = payment.user
        self.delivery_address = SQL.Get(Model_Delivery_Address, payment=payment)
        self.invoice_address = SQL.Get(Model_Invoice_Address, payment=payment)



class Sort_List:

    def Generate_Priority_List(self):
        priority_list = []

        for element in self.sort_list:

            # create vars
            payment_id = element[0]
            content = element[1]
            priority = 0

            # calculate priority for all words
            for word in self.words:
                priority += content.Calculate_Priority(word)

            # create list element
            priority_list.append((priority, payment_id))

        return priority_list

    def Create_List(self):

        for payment in self.payments:

            element = (
                payment.pk, # repetitions set range
                Payment_Content(payment)
            )

            self.sort_list.append(element)

    def __init__(self, payments, words):

        self.sort_list = []
        self.payments = payments
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
        return SQL.Filter(Model_Payment, pk__in=self.payments).extra(
            select={'sorting': sorting}, order_by=['sorting'])

    def Sort(self):

        # have no words
        if not self.words:
            return self.payments

        # have no products
        if not self.payments:
            return self.payments

        # generate priority list
        sort_list = Sort_List(self.payments, self.words)
        priority_list = sort_list.Generate_Priority_List()

        # sort products
        priority_list.sort(reverse=True)

        # select sorted products from database
        return self.__Get_Sorted_Products(priority_list)

    def __init__(self, search_engine):
        Base.__init__(self, search_engine)
        self.payments = search_engine.payments
        self.words = search_engine.words

