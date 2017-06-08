from arbuz.views import *
from user.forms import *
from user.account.forms import *
from payment.models import *


class Start_App(Dynamic_Event_Manager):

    def Manage_Content_Ground(self):

        self.content['apps'] = [
            {
                'name': Text(self.request, 58),
                'url':  self.Get_Path('user.account.details', current_language=True),
                'icon': '/_static/img/icons/128/dark/user_details.png',
            },
            {
                'name': Text(self.request, 59),
                'url': self.Get_Path('user.account.addresses', current_language=True),
                'icon': '/_static/img/icons/128/dark/id_card.png',
            },
            {
                'name': Text(self.request, 60),
                'url': self.Get_Path('user.account.my_shopping', current_language=True),
                'icon': '/_static/img/icons/128/dark/list_check.png',
            },
            {
                'name': Text(self.request, 61),
                'url': self.Get_Path('user.account.favorite', current_language=True),
                'icon': '/_static/img/icons/128/dark/badge.png',
            },
            {
                'name': Text(self.request, 62),
                'url': self.Get_Path('payment', current_language=True),
                'icon': '/_static/img/icons/128/dark/shopping_cart.png',
            },
        ]

        return self.Render_HTML('arbuz/start_app.html')

    @staticmethod
    def Launch(request):
        return Start_App(request, authorization=True).HTML



class Account_Details(Dynamic_Event_Manager):

    def Manage_Content_Ground(self):
        unique = self.request.session['user_unique']
        self.content['user'] = User.objects.get(unique=unique)
        return self.Render_HTML('user/account/details.html')

    def Manage_Form_Edit_Email(self):

        details = Form_User_Details(
            self.request, self.request.POST)

        if details.is_valid():
            unique = self.request.session['user_unique']
            user = User.objects.get(unique=unique)
            user.email = details.cleaned_data['new_email']
            user.save()

            return Dialog_Prompt(self.request, self.app_name, apply=True).HTML
        return Dialog_Prompt(self.request, self.app_name, not_valid=True).HTML

    def Manage_Form_Edit_Username(self):

        details = Form_User_Details(
            self.request, self.request.POST)

        if details.is_valid():
            unique = self.request.session['user_unique']
            user = User.objects.get(unique=unique)
            user.username = details.cleaned_data['new_username']
            user.save()

            return Dialog_Prompt(self.request, self.app_name, apply=True).HTML
        return Dialog_Prompt(self.request, self.app_name, not_valid=True).HTML

    def Manage_Form_Edit_Password(self):

        details = Form_User_Details(
            self.request, self.request.POST)

        if details.is_valid():
            unique = self.request.session['user_unique']
            user = User.objects.get(unique=unique)
            user.password = details.cleaned_data['new_password']
            user.save()

            return Dialog_Prompt(self.request, self.app_name, apply=True).HTML
        return Dialog_Prompt(self.request, self.app_name, not_valid=True).HTML

    def Manage_Form(self):

        if self.request.POST['__form__'] == 'edit_email':
            return self.Manage_Form_Edit_Email()

        if self.request.POST['__form__'] == 'edit_username':
            return self.Manage_Form_Edit_Username()

        if self.request.POST['__form__'] == 'edit_password':
            return self.Manage_Form_Edit_Password()

        return Dynamic_Event_Manager.Manage_Form(self)

    @staticmethod
    def Launch(request):
        return Account_Details(request, authorization=True).HTML



class User_Addresses(Dynamic_Event_Manager):

    def Get_User_Details(self):
        unique = self.request.session['user_unique']
        self.content['form_name_new'] = 'new_user_address'
        self.content['form_name_edit'] = 'edit_user_address'
        self.content['edit_forms_address'] = {}

        for address in User_Address.objects.filter(user=unique):
            self.content['edit_forms_address'][address.pk] = \
                Form_User_Address(self.request, instance=address)

    def Get_User_Address_ID(self):
        form_name = self.request.POST['__form__']
        id_address = int(form_name.replace('edit_user_address_', ''))

        if self.Check_ID_Address(id_address):
            return id_address

        raise Exception('An attempt unauthorized removal of address. '
                        '<user.Account.Get_User_Address_ID>')

    def Check_ID_Address(self, id_address):
        user = User.objects.get(unique=self.request.session['user_unique'])
        ids_address = User_Address.objects.filter(user=user).\
            values_list('id', flat=True)

        if id_address in ids_address:
            return True

        return False

    def Manage_Content_Ground(self):
        self.Get_User_Details()
        self.content['new_form_address'] = Form_User_Address(self.request)
        return self.Render_HTML('user/account/addresses.html')

    def Manage_Form_New_User_Address(self):

        self.content['form'] = Form_User_Address(self.request, self.request.POST)

        if self.content['form'].is_valid():
            unique = self.request.session['user_unique']
            address_user = self.content['form'].save(commit=False)
            address_user.user = User.objects.get(unique=unique)
            address_user.save()  # create address_user

            self.content['new_form_address'] = Form_User_Address(self.request)

        self.Get_User_Details()
        return self.Render_HTML('user/account/addresses.html')

    def Manage_Form_Edit_User_Address(self):

        id_address = self.Get_User_Address_ID()
        address = User_Address.objects.get(id=id_address)
        self.content['form'] = Form_User_Address(self.request,
             self.request.POST, instance=address)

        if self.content['form'].is_valid():
            self.content['form'].save() # save change of address_user

        self.Get_User_Details()
        self.content['new_form_address'] = Form_User_Address(self.request)
        return self.Render_HTML('user/account/addresses.html')

    def Manage_Form(self):

        if self.request.POST['__form__'] == 'new_user_address':
            return self.Manage_Form_New_User_Address()

        # all of edit forms
        if 'edit_user_address' in self.request.POST['__form__']:
            return self.Manage_Form_Edit_User_Address()

        return Dynamic_Event_Manager.Manage_Form(self)

    def Manage_Button(self):

        # removed address
        if '__button__' in self.request.POST:
            id_address = int(self.request.POST['value'])

            if self.Check_ID_Address(id_address):
                User_Address.objects.get(id=id_address).delete()
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



class My_Shopping(Dynamic_Event_Manager):

    def Get_Date(self):

        date_from = self.request.session['user_my_shopping_date_from']
        date_from = datetime.strptime(date_from, '%Y-%m-%d')
        date_to = self.request.session['user_my_shopping_date_to']
        date_to = datetime.strptime(date_to, '%Y-%m-%d')

        return date_from, date_to

    def Create_Payment_Structure(self):

        self.content['shopping'] = []

        date_from, date_to = self.Get_Date()
        user = User.objects.get(unique=self.request.session['user_unique'])
        payments = Payment.objects.filter(user=user, status='card',
                              date__gte=date_from, date__lte=date_to)

        for payment in payments:

            details = {
                'payment': payment,
                'full_name': Delivery_Address.objects.get(payment=payment).full_name,
                'products': Selected_Product.objects.filter(payment=payment)
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



class Favorite(Dynamic_Event_Manager):

    def Manage_Content_Ground(self):
        user = User.objects.get(unique=self.request.session['user_unique'])
        self.content['favorites'] = Product.objects.filter(
            pk__in=Favorite_Product.objects.filter(user=user).values('product__pk'))

        return self.Render_HTML('user/account/favorite.html')

    @staticmethod
    def Launch(request):
        return Favorite(request, authorization=True).HTML
