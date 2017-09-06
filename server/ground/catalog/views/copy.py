from server.ground.product.views.copy import *


class Copy_Catalog(Website_Manager):

    @staticmethod
    def Create_Copy_Catalog(from_catalog, name, language, parent):

        # create copy catalog
        copy_catalog = Model_Catalog()
        copy_catalog.name = name
        copy_catalog.url_name = Path_Manager.To_URL(name)
        copy_catalog.parent = parent
        copy_catalog.language = language
        SQL.Save(data=copy_catalog)

        # copy image
        copy_catalog.Copy_Image(from_catalog)
        return copy_catalog

    def Copy_Content_Recursive(self, from_catalog, copy_catalog, language):

        # copy products in current catalog
        products = SQL.Filter(Model_Product, parent=from_catalog)
        for child_product in products:

            # copy child product
            Copy_Product.Create_Copy_Product(child_product,
                child_product.name, language, copy_catalog)

        # copy catalogs
        catalogs = SQL.Filter(Model_Catalog, parent=from_catalog)
        for child_catalog in catalogs:

            # create copy child catalog
            child_copy_catalog = self.Create_Copy_Catalog(
                child_catalog, child_catalog.name, language, copy_catalog)

            # copy content child copy catalog
            self.Copy_Content_Recursive(child_catalog,
                child_copy_catalog, language)

    def Manage_Form(self):

        self.context['form'] = Form_Copy(self, post=True)
        if self.context['form'].is_valid():

            # get data
            from_catalog = self.request.session['catalog_copy_element']
            language = self.request.POST['language']
            name = self.request.POST['name']

            # create copy catalog
            copy_catalog = self.Create_Copy_Catalog(
                from_catalog, name, language, from_catalog.parent)

            # copy content
            self.Copy_Content_Recursive(from_catalog, copy_catalog, language)

            return Dialog_Prompt(self, apply=True).HTML
        return Dialog_Prompt(self, not_valid=True).HTML

    @staticmethod
    def Launch(request):
        return Copy_Catalog(request, only_root=True).HTML
