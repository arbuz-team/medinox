from server.manage.switch.website.manager import *
from server.manage.switch.pages import *
from server.service.searcher.views import *


class Products(Website_Manager):

    def Selected_Products(self):
        products = self.request.session['searcher_result']

        # no selected products
        # search it
        if not products:

            phrase = self.request.session['searcher_phrase']
            engine = Search_Engine(self, phrase)
            products = engine.Search_Products()

            # save selected product to session
            self.request.session['searcher_result'] = products

        return products

    def Manage_Content(self):

        # get data
        products = self.Selected_Products()
        numberon_page = self.request.session['product_number_on_page']
        selected_page = self.request.session['product_page']

        # get page of products
        pages_manager = Pages_Manager(
            products, numberon_page, selected_page)

        # append page to context
        self.context.update(pages_manager.Create_Pages())
        return self.Render_HTML('product/products.html')

    def Manage_Button(self):

        self.request.session['product_page'] = \
            int(self.request.POST['value'])

        return HttpResponse()

    @staticmethod
    def Launch(request):
        return Products(request).HTML
