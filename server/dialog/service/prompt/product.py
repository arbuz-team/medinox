from server.dialog.service.base import *


class Service_Product(Base_Service):

    def New(self):

        self.request.session['product_product'] = Model_Product()
        self.request.session['product_is_editing'] = False

    def Edit(self):

        product = SQL.Get(Model_Product,
            pk=self.request.POST['value'])

        self.request.session['product_is_editing'] = True
        self.request.session['product_product'] = product

        self.context['edit'] = {'url': '/product/manage/'}
        self.context['image'] = product.image
        self.initial = {
            'name': product.name,
            'price': product.price,
            'brand': product.brand,
        }

    def Manage(self):

        if self.request.POST['value']:
            self.Edit()

        else: self.New()

        self.context['title'] = Text(self, 158)
        self.context['form'] = self.Prepare_Form(
            Form_Product, initial=self.initial)

        return self.Render_Dialog(
            'product.html', 'product', only_root=True)