from server.dialog.service.base import *
from server.ground.product.forms import *


class Service_Widget(Base_Service):

    def New(self):
        pass

    def Edit(self):

        # get number
        if 'value' in self.request.POST:
            if self.request.POST['value']:

                widget = self.request.POST['value']
                self.instance = SQL.Get(Model_Widget, pk=widget)
                self.context['edit'] = {'url': '/product/widget/manage/'}

        # other value get widget to edit
        # after created widget - next dialog
        elif self.dialog.other_value:
            self.instance = self.dialog.other_value
            self.context['edit'] = {'url': '/product/widget/manage/'}

        # second form for append options to widget
        if self.instance:
            self.context['additional_form'] = \
                self.Prepare_Form(Form_Values)

    def Not_Valid(self):
        self.context['title'] = Text(self, 156)
        return self.Render_Dialog(
            'widget.html', 'widget', 'values', only_root=True)

    def Manage(self):

        # check if edit widget
        self.Edit()

        # code for each widget
        self.request.session['product_widget'] = self.instance
        self.context['values'] = SQL.Filter(Model_Values, widget=self.instance)
        self.context['title'] = Text(self, 156)
        self.context['form'] = self.Prepare_Form(
            Form_Widget, instance=self.instance)

        return self.Render_Dialog(
            'widget.html', 'widget', 'values', only_root=True)
