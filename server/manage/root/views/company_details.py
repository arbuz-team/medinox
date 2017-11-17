from server.manage.switch.website.manager import *
from server.manage.root.forms import *
from server.service.payment.forms import *


class Company_Details_Manager(Website_Manager):

    def Manage_Content(self):

        data = SQL.First(Model_Data_For_Public)
        self.context['display_shop_address'] = data.shop_address

        company_address = SQL.First(Model_Root_Address)
        shop_address = SQL.First(Model_Shop_Address)

        self.context['form'] = Form_Root_Address(self, instance=company_address)
        self.context['additional_form'] = Form_Shop_Address(self, instance=shop_address)

        return self.Render_HTML('root/company_details.html', 'root_address', 'shop_address')

    def Manage_Form_Root_Address(self):

        data = SQL.First(Model_Data_For_Public)
        self.context['display_shop_address'] = data.shop_address

        # shop address
        shop_address = SQL.First(Model_Shop_Address)
        self.context['additional_form'] = \
            Form_Root_Address(self, instance=shop_address)

        company_address = SQL.First(Model_Root_Address)
        self.context['form'] = Form_Root_Address(
            self, post=True, instance=company_address)

        if self.context['form'].is_valid():
            company_address = self.context['form'].save(commit=False) # save change of address_user
            SQL.Save(data=company_address)

            return self.Render_HTML('root/company_details.html', 'root_address', 'shop_address')
        return self.Render_HTML('root/company_details.html', 'root_address', 'shop_address')

    def Manage_Form_Shop_Address(self):

        data = SQL.First(Model_Data_For_Public)
        self.context['display_shop_address'] = data.shop_address

        company_address = SQL.First(Model_Root_Address)
        self.context['form'] = Form_Root_Address(
            self, instance=company_address)

        shop_address = SQL.First(Model_Shop_Address)
        self.context['additional_form'] = Form_Shop_Address(
            self, post=True, instance=shop_address)

        if self.context['additional_form'].is_valid():
            shop_address = self.context['additional_form'].save(commit=False) # save change of address_user
            SQL.Save(data=shop_address)

            return self.Render_HTML('root/company_details.html', 'root_address', 'shop_address')
        return self.Render_HTML('root/company_details.html', 'root_address', 'shop_address')

    def Manage_Form(self):

        if self.request.POST['_name_'] == 'root_address':
            return self.Manage_Form_Root_Address()

        if self.request.POST['_name_'] == 'shop_address':
            return self.Manage_Form_Shop_Address()

        return Website_Manager.Manage_Form(self)

    def Manage_Button(self):

        if self.request.POST['_name_'] == 'display_shop_address':
            value = self.request.POST['value']

            data = SQL.First(Model_Data_For_Public)
            data.shop_address = True if value == 'true' else False
            SQL.Save(data=data)

            return HttpResponse()

    @staticmethod
    def Launch(request):
        return Company_Details_Manager(request, only_root=True).HTML
