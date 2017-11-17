from server.ground.catalog.models import *


class Catalog_Tree(Base):

    @staticmethod
    def Have_Children(element):
        return True if SQL.Filter(
            Model_Catalog, parent=element) else False

    def Render_Catalog(self, catalog, children):
        self.context['parent'] = catalog
        self.context['catalogs'] = list(range(children.count()))
        self.context['have_children'] = self.Have_Children(catalog)
        return self.Render_To_String(self.html_tree)

    def Recursive_Catalogs(self, parent, language):

        catalogs = SQL.Filter(Model_Catalog, parent=parent, language=language)
        tree = self.Render_Catalog(parent, catalogs)

        for index, catalog in enumerate(catalogs):

            tree = tree.replace(
                '<{0}>'.format(index),
                self.Recursive_Catalogs(catalog, language)
            )

        return tree

    def Create_Catalog_Tree(self, language):
        root_catalog = SQL.Get(Model_Catalog, parent=None, name='/')
        return self.Recursive_Catalogs(root_catalog, language)

    def __init__(self, _object, html_tree):
        Base.__init__(self, _object)
        self.html_tree = html_tree