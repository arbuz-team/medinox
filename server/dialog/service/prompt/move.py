from server.dialog.service.base import *
from server.ground.catalog.forms.operation import *


class Service_Move(Base_Service):

    @staticmethod
    def Have_Children(element):
        return True if SQL.Filter(
            Model_Catalog, parent=element) else False

    def Get_Element(self):

        if 'value' in self.request.POST:
            element_type = self.dialog.Get_Post_Other('type')
            element_pk = self.request.POST['value']

            # get element
            if element_type == 'product':
                return SQL.Get(Model_Product, pk=element_pk)

            if element_type == 'catalog':
                return SQL.Get(Model_Catalog, pk=element_pk)

        return self.request.session['catalog_move_element']

    def New(self):

        # get post data
        element_type = self.dialog.Get_Post_Other('type')
        element = self.Get_Element()

        # initial data
        self.request.session['catalog_move_element'] = element
        self.request.session['catalog_move_type'] = element_type
        language = self.request.session['translator_language']

        self.initial = {
            'language': language,
            'name': element.name
        }

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

    def Manage(self):

        self.Create_Catalog_Tree()
        self.New()

        # code for each widget
        self.context['title'] = Text(self, 179)
        self.context['form'] = self.Prepare_Form(
            Form_Move, initial=self.initial)

        return self.Render_Dialog(
            'move.html', 'move', only_root=True)
