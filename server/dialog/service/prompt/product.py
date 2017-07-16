from server.dialog.service.base import *


class Service_Product(Base_Service):

    def New(self):

        self.request.session['product_product'] = Product()
        self.request.session['product_is_editing'] = False

    def Edit(self):

        product = SQL.Get(Product,
            pk=self.request.POST['dialog_value'])

        self.request.session['product_is_editing'] = True
        self.request.session['product_product'] = product

        self.content['edit'] = {'url': '/product/manage/'}
        self.content['image'] = product.image
        self.initial = {
            'name': product.name,
            'price': product.price,
            'brand': product.brand,
        }

    def Manage(self):

        if 'dialog_value' in self.request.POST:
            self.Edit()

        else: self.New()

        self.content['title'] = Text(self, 158)
        self.content['form'] = self.Prepare_Form(
            Form_Product, initial=self.initial)

        return self.Render_Dialog(
            'product.html', 'product', only_root=True)