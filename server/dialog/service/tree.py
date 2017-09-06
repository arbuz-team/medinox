from server.dialog.service.base import *
from server.ground.catalog.models import *


class Catalog_Tree(Base_Service, metaclass=ABCMeta):

    @staticmethod
    def Have_Children(element):
        return True if SQL.Filter(
            Model_Catalog, parent=element) else False

    def Render_Catalog(self, catalog, children):
        self.context['parent'] = catalog
        self.context['catalogs'] = list(range(children.count()))
        self.context['have_children'] = self.Have_Children(catalog)
        return self.Render_To_String('catalog/tree.html')

    def Recursive_Catalogs(self, parent):

        catalogs = SQL.Filter(Model_Catalog, parent=parent)
        tree = self.Render_Catalog(parent, catalogs)

        for index, catalog in enumerate(catalogs):

            tree = tree.replace(
                '<{0}>'.format(index),
                self.Recursive_Catalogs(catalog)
            )

        return tree

    def Create_Catalog_Tree(self):

        root_catalog = SQL.Get(Model_Catalog,
           parent=None, name='/')

        self.context['catalog_tree'] = \
            self.Recursive_Catalogs(root_catalog)
