from server.manage.switch.website.manager import *
from server.content.product.forms import *
from server.manage.switch.position import *


class Values_Manager(Website_Manager):

    def Manage_Form(self):
        self.content['form'] = Form_Values(self, post=True)

        if self.content['form'].is_valid():
            widget = self.request.session['product_widget']

            values = self.content['form'].save(commit=False)
            values.widget = widget
            SQL.Save(data=values)

            return Dialog_Prompt(self.request, self.app_name, other_value=widget).HTML
        return Dialog_Prompt(self.request, self.app_name, not_valid=True).HTML

    def Manage_Button(self):

        if 'delete' in self.request.POST['__button__']:
            SQL.Delete(Values, pk=self.request.POST['value'])
            return JsonResponse({'__button__': 'true'})

        return JsonResponse({'__button__': 'false'})

    @staticmethod
    def Launch(request):
        return Product_Manager(request, only_root=True).HTML
