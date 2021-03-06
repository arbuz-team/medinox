from server.manage.switch.website.manager import *
from server.ground.product.forms import *
from server.manage.switch.position import *


class Description_Manager(Website_Manager):

    def Manage_Form_Description(self):
        description = Form_Description(self, post=True)

        if description.is_valid():

            product_desc = self.request.session['product_description']
            position_manager = Position_Manager(self)
            position_manager.Insert_Element(Model_Description, product_desc)

            product_desc.header = description.cleaned_data['header']
            product_desc.paragraph = description.cleaned_data['paragraph']
            product_desc.product = self.request.session['product_last_selected']
            SQL.Save(data=product_desc)

            product_desc.Save_Image(description.cleaned_data['image'])

            return Dialog_Prompt(self, apply=True).HTML
        return Dialog_Prompt(self, not_valid=True).HTML

    def Manage_Form(self):

        if self.request.POST['_name_'] == 'description':
            return self.Manage_Form_Description()

        return Website_Manager.Manage_Form(self)

    def Manage_Button(self):

        if self.request.POST['_name_'] == 'delete_image':
            description = self.request.session['product_description']
            description.image = None
            SQL.Save(data=description)
            return HttpResponse()

        else:

            position_manager = Position_Manager(self)
            position_manager.Button_Service(Model_Description)
            return HttpResponse()

    @staticmethod
    def Launch(request):
        return Description_Manager(request, only_root=True).HTML

