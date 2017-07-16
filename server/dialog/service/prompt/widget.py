from server.dialog.service.base import *


class Service_Widget(Base_Service):

    def New(self):
        pass

    def Edit(self):

        # get number
        if 'dialog_value' in self.request.POST:

            widget = self.request.POST['dialog_value']
            self.instance = SQL.Get(Widget, pk=widget)
            self.content['edit'] = {'url': '/product/widget/manage/'}

        # other value get widget to edit
        # after created widget - next dialog
        elif self.dialog.other_value:
            self.instance = self.dialog.other_value

        # second form for append options to widget
        if self.instance:
            self.content['additional_form'] = \
                self.Prepare_Form(Form_Values)

    def Manage(self):

        # check if edit widget
        self.Edit()

        # code for each widget
        self.request.session['product_widget'] = self.instance
        self.content['values'] = SQL.Filter(Values, widget=self.instance)
        self.content['title'] = Text(self, 156)
        self.content['form'] = self.Prepare_Form(
            Form_Widget, instance=self.instance)

        return self.Render_Dialog(
            'widget.html', 'widget', 'values', only_root=True)
