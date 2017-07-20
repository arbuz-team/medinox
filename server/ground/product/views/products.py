from server.manage.switch.website.manager import *
from server.manage.switch.position import *
from server.manage.switch.pages import *


class Products(Website_Manager):

    def Manage_Content(self):

        products = self.request.session['searcher_result']
        number_product_on_page = self.request.session['product_number_product_on_page']
        selected_page = self.request.session['product_page']

        pages_manager = Pages_Manager(
            products, number_product_on_page, selected_page)

        self.context.update(pages_manager.Create_Pages())
        return self.Render_HTML('product/products.html')

    def Manage_Button(self):

        self.request.session['product_page'] = \
            int(self.request.POST['value'])

        return HttpResponse()

    @staticmethod
    def Launch(request):
        return Products(request).HTML
