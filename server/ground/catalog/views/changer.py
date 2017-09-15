from server.manage.session.views import *


class Catalog_Not_Found(Exception):
    pass



class Catalog_Changer(Base):

    @staticmethod
    def Get_Catalog(url_name, parent):

        if url_name:

            cat = SQL.Filter(Model_Catalog,
                url_name=url_name, parent=parent)

            if cat: return cat[0]
            else: raise Catalog_Not_Found()

        return None

    def Get_Selected_Catalog(self):

        catalogs = self.catalog_path.split('/')[:-1]
        parent = SQL.Get(Model_Catalog, parent=None, name='/')
        selected = SQL.Get(Model_Catalog, parent=None, name='/')

        # search selected catalog
        for catalog in catalogs:
            selected = self.Get_Catalog(catalog, parent)
            parent = selected

        return selected

    def Change_Catalog(self):

        catalog = self.Get_Selected_Catalog()
        self.request.session['catalog_parent'] = catalog
        self.request.session['catalog_path'] = self.catalog_path

    def __init__(self, request, catalog_path):
        Check_Session(request)

        self.request = request
        self.catalog_path = catalog_path

        Base.__init__(self, self)
        self.Change_Catalog()
