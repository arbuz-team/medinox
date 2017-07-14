from server.content.product.views import *
from server.content.catalog.forms import *


class Catalog_Changer(Website_Manager):

    @staticmethod
    def Get_Catalog(url_name, parent):

        if url_name:

            cat = SQL.Filter(Model_Catalog,
                url_name=url_name, parent=parent)

            if cat: return cat[0]
            else: raise Exception('Catalog not exists')

        return None

    def Get_Selected_Catalog(self):

        catalogs = self.catalog_path.split('/')[:-1]
        parent = None
        selected = None

        if not catalogs:
            return None

        for catalog in catalogs:
            selected = self.Get_Catalog(catalog, parent)
            parent = selected

        return selected

    def Change_Catalog(self):

        try: catalog = self.Get_Selected_Catalog()
        except: return Statement_404.Launch(self.request)

        self.request.session['catalog_parent'] = catalog
        self.request.session['catalog_path'] = self.catalog_path

    def __init__(self, request, catalog_path):
        Website_Manager.__init__(self, request)

        self.catalog_path = catalog_path
        self.Change_Catalog()
