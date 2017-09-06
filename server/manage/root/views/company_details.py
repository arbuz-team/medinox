from server.manage.switch.website.manager import *
from server.manage.root.forms import *
from server.service.payment.forms import *


class Company_Details_Manager(Website_Manager):

    def Manage_Content(self):
        address = SQL.First(Model_Root_Address)
        self.context['form'] = Form_Root_Address(self, instance=address)
        return self.Render_HTML('root/company_details.html', 'root_address')

    def Manage_Form_Root_Address(self):

        address = SQL.First(Model_Root_Address)
        self.context['form'] = Form_Root_Address(
            self, post=True, instance=address)

        if self.context['form'].is_valid():
            address = self.context['form'].save(commit=False) # save change of address_user
            SQL.Save(data=address)

            return self.Render_HTML('root/company_details.html', 'root_address')
        return self.Render_HTML('root/company_details.html', 'root_address')

    def Manage_Form(self):

        if self.request.POST['_name_'] == 'root_address':
            return self.Manage_Form_Root_Address()

        return Website_Manager.Manage_Form(self)

    @staticmethod
    def Launch(request):
        return Company_Details_Manager(request, only_root=True).HTML
