from server.manage.switch.website import *
from server.ground.link.forms import *


class Copy_Link(Website_Manager):

    @staticmethod
    def Create_Copy_Link(from_link, target):
        link = None

        if from_link.__class__ == Model_Product_Link:
            link = Model_Product_Link(product=from_link.product,
                  parent=target, language=from_link.language)

        if from_link.__class__ == Model_Catalog_Link:
            link = Model_Catalog_Link(catalog=from_link.catalog,
                  parent=target, language=from_link.language)

        SQL.Save(data=link)

    def Manage_Form(self):

        self.context['form'] = Form_Link(self, post=True)
        if self.context['form'].is_valid():

            # get data
            from_link = self.request.session['catalog_copy_element']
            target = SQL.Get(Model_Catalog, pk=self.request.POST['target'])

            # create copy product
            self.Create_Copy_Link(from_link, target)

            return Dialog_Prompt(self, apply=True).HTML
        return Dialog_Prompt(self, not_valid=True).HTML

    @staticmethod
    def Launch(request):
        return Copy_Link(request, only_root=True).HTML
