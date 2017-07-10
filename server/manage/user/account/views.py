from server.manage.switch.views import *
from server.manage.user.forms import *
from server.manage.user.account.forms import *
from server.service.payment.models import *


class Panel_App(Website_Manager):

    def Manage_Content_Ground(self):

        path_manager = Path_Manager(self)
        self.content['apps'] = [
            {
                'name': Text(self, 58),
                'url':  path_manager.Get_Path('user.account.details', current_language=True),
                'icon': '/static/img/icons/128/dark/user_details.png',
            },
            {
                'name': Text(self, 59),
                'url': path_manager.Get_Path('user.account.addresses', current_language=True),
                'icon': '/static/img/icons/128/dark/id_card.png',
            },
            {
                'name': Text(self, 60),
                'url': path_manager.Get_Path('user.account.my_shopping', current_language=True),
                'icon': '/static/img/icons/128/dark/list_check.png',
            },
            {
                'name': Text(self, 61),
                'url': path_manager.Get_Path('user.account.favorite', current_language=True),
                'icon': '/static/img/icons/128/dark/badge.png',
            },
            {
                'name': Text(self, 62),
                'url': path_manager.Get_Path('payment', current_language=True),
                'icon': '/static/img/icons/128/dark/shopping_cart.png',
            },
        ]

        return self.Render_HTML('arbuz/panel_app.html')

    @staticmethod
    def Launch(request):
        return Panel_App(request, authorization=True).HTML



class Account_Details(Website_Manager):

    def Manage_Content_Ground(self):
        self.content['user'] = self.request.session['user_user']
        return self.Render_HTML('user/account/details.html')

    def Manage_Form_Edit_Email(self):

        details = Form_User_Details(
            self.request, self.request.POST)

        if details.is_valid():
            user = self.request.session['user_user']
            user.email = details.cleaned_data['new_email']
            SQL.Save(data=user)

            return Dialog_Prompt(self.request, self.app_name, apply=True).HTML
        return Dialog_Prompt(self.request, self.app_name, not_valid=True).HTML

    def Manage_Form_Edit_Username(self):

        details = Form_User_Details(
            self.request, self.request.POST)

        if details.is_valid():
            user = self.request.session['user_user']
            user.username = details.cleaned_data['new_username']
            SQL.Save(data=user)

            return Dialog_Prompt(self.request, self.app_name, apply=True).HTML
        return Dialog_Prompt(self.request, self.app_name, not_valid=True).HTML

    def Manage_Form_Edit_Password(self):

        details = Form_User_Details(
            self.request, self.request.POST)

        if details.is_valid():
            user = self.request.session['user_user']
            user.password = details.cleaned_data['new_password']
            SQL.Save(data=user)

            return Dialog_Prompt(self.request, self.app_name, apply=True).HTML
        return Dialog_Prompt(self.request, self.app_name, not_valid=True).HTML

    def Manage_Form(self):

        if self.request.POST['__form__'] == 'email':
            return self.Manage_Form_Edit_Email()

        if self.request.POST['__form__'] == 'username':
            return self.Manage_Form_Edit_Username()

        if self.request.POST['__form__'] == 'password':
            return self.Manage_Form_Edit_Password()

        return Website_Manager.Manage_Form(self)

    @staticmethod
    def Launch(request):
        return Account_Details(request, authorization=True).HTML



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



class My_Shopping(Website_Manager):

    def Get_Date(self):

        date_from = self.request.session['user_my_shopping_date_from']
        date_from = datetime.strptime(date_from, '%Y-%m-%d')
        date_to = self.request.session['user_my_shopping_date_to']
        date_to = datetime.strptime(date_to, '%Y-%m-%d')

        return date_from, date_to

    def Create_Payment_Structure(self):

        self.content['shopping'] = []

        date_from, date_to = self.Get_Date()
        user = self.request.session['user_user']
        payments = SQL.Filter(Payment, user=user, status='cart',
                              date__gte=date_from, date__lte=date_to)

        for payment in payments:

            details = {
                'payment': payment,
                'full_name': SQL.Get(Delivery_Address, payment=payment).full_name,
                'products': SQL.Filter(Selected_Product, payment=payment)
            }

            self.content['shopping'].append(details)

    def Manage_Content_Ground(self):
        self.Create_Payment_Structure()
        self.content['date_from'] = self.request.session['user_my_shopping_date_from']
        self.content['date_to'] = self.request.session['user_my_shopping_date_to']
        self.content['button_address_name'] = 'user_address'
        return self.Render_HTML('user/account/my_shopping.html')

    def Manage_Filter(self):

        if self.request.POST['__filter__'] == 'date_to':
            self.request.session['user_my_shopping_date_to'] = \
                self.request.POST['value']

        if self.request.POST['__filter__'] == 'date_from':
            self.request.session['user_my_shopping_date_from'] = \
                self.request.POST['value']

        self.Validate_Period('user_my_shopping_date_from', 'user_my_shopping_date_to')
        return JsonResponse({'__filter__': 'true'})

    @staticmethod
    def Launch(request):
        return My_Shopping(request, authorization=True).HTML



class Favorite(Website_Manager):

    def Manage_Content_Ground(self):
        user = self.request.session['user_user']
        self.content['favorites'] = SQL.Filter(Product,
            pk__in=SQL.Filter(Favorite_Product, user=user).values('product__pk'))

        return self.Render_HTML('user/account/favorite.html')

    @staticmethod
    def Launch(request):
        return Favorite(request, authorization=True).HTML
