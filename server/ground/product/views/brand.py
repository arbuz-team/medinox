from server.manage.switch.website.manager import *
from server.ground.product.forms import *


class Brand_Manager(Website_Manager):

    def Manage_Form(self):
        # self.context['form'] = Form_Brand(self, post=True)

        if self.context['form'].is_valid():
            brand = self.request.session['product_brand']
            brand.name = self.context['form'].cleaned_data['name']
            SQL.Save(data=brand)

            return Dialog_Prompt(self, other_value=widget).HTML
        return Dialog_Prompt(self, not_valid=True).HTML

    def Manage_Button(self):

        if 'delete' in self.request.POST['_name_']:
            SQL.Delete(Model_Brand, pk=self.request.POST['value'])
            return HttpResponse()

    @staticmethod
    def Launch(request):
        return Brand_Manager(request, only_root=True).HTML
