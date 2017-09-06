from server.manage.switch.website.manager import *
from server.ground.product.forms import *
from server.manage.switch.position import *


class Widget_Manager(Website_Manager):

    def Manage_Form_New_Widget(self):
        self.context['form'] = Form_Widget(self, post=True)

        if self.context['form'].is_valid():
            widget = Model_Widget(product=self.request.session['product_last_selected'])
            widget.name = self.context['form'].cleaned_data['name']
            widget.type = self.context['form'].cleaned_data['type']
            SQL.Save(data=widget)

            # other value get widget to edit
            return Dialog_Prompt(self, other_value=widget).HTML
        return Dialog_Prompt(self, not_valid=True).HTML

    def Manage_Form_Edit_Widget(self):
        self.context['form'] = Form_Widget(self, post=True)

        if self.context['form'].is_valid():
            widget = self.request.session['product_widget']
            widget.name = self.context['form'].cleaned_data['name']
            widget.type = self.context['form'].cleaned_data['type']
            SQL.Save(data=widget)

            return Dialog_Prompt(self, apply=True).HTML
        return Dialog_Prompt(self, not_valid=True).HTML

    def Manage_Form(self):

        if self.request.session['product_widget']:
            return self.Manage_Form_Edit_Widget()

        return self.Manage_Form_New_Widget()

    def Manage_Button(self):

        if 'delete' in self.request.POST['_name_']:
            SQL.Delete(data=self.request.session['product_widget'])
            self.request.session['product_widget'] = None
            return HttpResponse()

    @staticmethod
    def Launch(request):
        return Widget_Manager(request, only_root=True).HTML
