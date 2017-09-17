from server.manage.switch.website.manager import *
from server.ground.product.forms import *
from server.manage.switch.position import *


class Values_Manager(Website_Manager):

    def Manage_Form(self):
        self.context['form'] = Form_Values(self, post=True)

        if self.context['form'].is_valid():
            widget = self.request.session['product_widget']

            values = self.context['form'].save(commit=False)
            values.widget = widget
            SQL.Save(data=values)

            return Dialog_Prompt(self, other_value=widget).HTML
        return Dialog_Prompt(self, not_valid=True).HTML

    def Manage_Button(self):

        if 'delete_widget_option' in self.request.POST['_name_']:
            SQL.Delete(Model_Values, pk=self.request.POST['value'])
            return HttpResponse()

    @staticmethod
    def Launch(request):
        return Product_Manager(request, only_root=True).HTML
