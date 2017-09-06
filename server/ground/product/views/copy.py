from server.manage.switch.website.manager import *
from server.ground.catalog.forms.operation import *


class Copy_Product(Website_Manager):

    @staticmethod
    def Create_Copy_Product(from_product, name, language, parent):

        # create copy product
        copy_product = Model_Product()
        copy_product.name = name
        copy_product.url_name = Path_Manager.To_URL(name)
        copy_product.price = from_product.price
        copy_product.parent = parent
        copy_product.language = language
        SQL.Save(data=copy_product)

        # copy image
        copy_product.Copy_Image(from_product)

    def Manage_Form(self):

        self.context['form'] = Form_Copy(self, post=True)
        if self.context['form'].is_valid():

            # get data
            from_product = self.request.session['catalog_copy_element']
            language = self.request.POST['language']
            name = self.request.POST['name']

            # create copy product
            self.Create_Copy_Product(from_product, name,
                 language, from_product.parent)

            return Dialog_Prompt(self, apply=True).HTML
        return Dialog_Prompt(self, not_valid=True).HTML

    @staticmethod
    def Launch(request):
        return Copy_Product(request, only_root=True).HTML
