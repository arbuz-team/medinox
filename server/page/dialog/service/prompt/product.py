from server.page.dialog.service.base import *


class Service_Product(Base_Service):

    def New(self):

        self.request.session['product_product'] = Product()
        self.request.session['product_is_editing'] = False

    def Edit(self):

        product = Product.objects.get(
            pk=self.request.POST['dialog_value'])

        self.request.session['product_is_editing'] = True
        self.request.session['product_product'] = product

        self.content['edit'] = {'url': '/product/manage/'}
        self.content['image'] = product.image
        self.instance = {'name': product.name}

    def Manage(self):

        if 'dialog_value' in self.request.POST:
            self.Edit()

        else: self.New()

        self.content['title'] = Text(self.request, 158)
        self.content['form'] = self.Prepare_Form(
            Form_Product, instance=self.instance)

        return self.dialog.Render_Dialog(
            'dialog/product.html', 'product', only_root=True)