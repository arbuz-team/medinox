from server.manage.switch.website.manager import *
from server.manage.user.forms import *
from server.manage.user.account.forms import *


class User_Addresses(Website_Manager):

    def Get_User_Details(self):
        unique = self.request.session['user_user'].unique
        self.content['form_name_new'] = 'new_user_address'
        self.content['form_name_edit'] = 'edit_user_address'
        self.content['edit_forms_address'] = {}

        for address in SQL.Filter(User_Address, user=unique):
            self.content['edit_forms_address'][address.pk] = \
                Form_User_Address(self, instance=address)

    def Get_User_Address_ID(self):
        form_name = self.request.POST['__form__']
        id_address = int(form_name.replace('edit_user_address_', ''))

        if self.Check_ID_Address(id_address):
            return id_address

        raise Exception('An attempt unauthorized removal of address. '
                        '<user.Account.Get_User_Address_ID>')

    def Check_ID_Address(self, id_address):
        user = self.request.session['user_user']
        ids_address = SQL.Filter(User_Address, user=user).\
            values_list('id', flat=True)

        if id_address in ids_address:
            return True

        return False

    def Manage_Content_Ground(self):
        self.Get_User_Details()
        self.content['new_form_address'] = Form_User_Address(self)
        return self.Render_HTML('user/account/addresses.html')

    def Manage_Form_New_User_Address(self):
        self.content['form'] = Form_User_Address(self, post=True)

        if self.content['form'].is_valid():
            address_user = self.content['form'].save(commit=False)
            address_user.user = self.request.session['user_user']
            SQL.Save(data=address_user)  # create address_user

            self.content['new_form_address'] = Form_User_Address(self)

        self.Get_User_Details()
        return self.Render_HTML('user/account/addresses.html')

    def Manage_Form_Edit_User_Address(self):

        id_address = self.Get_User_Address_ID()
        address = SQL.Get(User_Address, id=id_address)
        self.content['form'] = Form_User_Address(
            self, post=True, instance=address)

        if self.content['form'].is_valid():
            address = self.content['form'].save(commit=False) # save change of address_user
            SQL.Save(data=address)

        self.Get_User_Details()
        self.content['new_form_address'] = Form_User_Address(self)
        return self.Render_HTML('user/account/addresses.html')

    def Manage_Form(self):

        if self.request.POST['__form__'] == 'new_user_address':
            return self.Manage_Form_New_User_Address()

        # all of edit forms
        if 'edit_user_address' in self.request.POST['__form__']:
            return self.Manage_Form_Edit_User_Address()

        return Website_Manager.Manage_Form(self)

    def Manage_Button(self):

        # removed address
        if '__button__' in self.request.POST:
            id_address = int(self.request.POST['value'])

            if self.Check_ID_Address(id_address):
                SQL.Delete(User_Address, id=id_address)
                return JsonResponse({'__button__': 'true'})

        return JsonResponse({'__button__': 'false'})

    @staticmethod
    def Redirect(request, url):
        other_value = {'redirect': url}
        return User_Addresses(request, other_value=other_value,
                              length_navigation=3).HTML

    @staticmethod
    def Launch(request):
        return User_Addresses(request, authorization=True).HTML
