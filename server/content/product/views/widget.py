from server.manage.switch.website.manager import *
from server.content.product.forms import *
from server.manage.switch.position import *


class Widget_Manager(Website_Manager):

    def Manage_Form_New_Widget(self):
        self.content['form'] = Form_Widget(self, post=True)

        if self.content['form'].is_valid():
            widget = Widget(product=self.request.session['product_last_selected'])
            widget.name = self.content['form'].cleaned_data['name']
            widget.type = self.content['form'].cleaned_data['type']
            SQL.Save(data=widget)

            # other value get widget to edit
            return Dialog_Prompt(self.request, self.app_name, other_value=widget).HTML
        return Dialog_Prompt(self.request, self.app_name, not_valid=True).HTML

    def Manage_Form_Edit_Widget(self):
        self.content['form'] = Form_Widget(self, post=True)

        if self.content['form'].is_valid():
            widget = self.request.session['product_widget']
            widget.name = self.content['form'].cleaned_data['name']
            widget.type = self.content['form'].cleaned_data['type']
            SQL.Save(data=widget)

            return Dialog_Prompt(self.request, self.app_name, apply=True).HTML
        return Dialog_Prompt(self.request, self.app_name, not_valid=True).HTML

    def Manage_Form(self):

        if self.request.session['product_widget']:
            return self.Manage_Form_Edit_Widget()

        return self.Manage_Form_New_Widget()

    def Manage_Button(self):

        if 'delete' in self.request.POST['__button__']:
            self.request.session['product_widget'].delete()
            self.request.session['product_widget'] = None
            return JsonResponse({'__button__': 'true'})

        return JsonResponse({'__button__': 'false'})

    @staticmethod
    def Launch(request):
        return Widget_Manager(request, only_root=True).HTML
