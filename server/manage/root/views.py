from server.manage.switch.views import *
from server.manage.root.forms import *
from server.service.payment.models import *


class Start_App(Dynamic_Event_Manager):

    def Manage_Content_Ground(self):

        self.content['apps'] = [
            {
                'name': Text(self.request, 24),
                'url': self.Get_Path('root.sign_out', current_language=True),
                'icon': '/static/img/icons/128/dark/logout.png',
            },
            {
                'name': Text(self.request, 25),
                'url': self.Get_Path('root.company_details', current_language=True),
                'icon': '/static/img/icons/128/dark/moustache.png',
            },
            {
                'name': Text(self.request, 27),
                'url': self.Get_Path('root.users_payments', current_language=True),
                'icon': '/static/img/icons/128/dark/money.png',
            },
            {
                'name': Text(self.request, 135),
                'url': self.Get_Path('root.social_media', current_language=True),
                'icon': '/static/img/icons/128/dark/social_group.png',
            },
            {
                'name': Text(self.request, 136),
                'url': self.Get_Path('root.delivery_settings', current_language=True),
                'icon': '/static/img/icons/128/dark/transport.png',
            },
        ]

        return self.Render_HTML('arbuz/start_app.html')

    @staticmethod
    def Launch(request):
        return Start_App(request, only_root=True).HTML



class Sign_In(Dynamic_Event_Manager):

    def Manage_Content_Ground(self):
        self.content['form'] = Form_Root_Login(self.request)
        return self.Render_HTML('root/sign_in.html', 'login')

    def Manage_Form_Login(self):

        self.content['form'] = \
            Form_Root_Login(self.request, self.request.POST)

        if self.content['form'].is_valid():
            self.request.session['root_login'] = True
            self.request.session['main_number_product_on_page'] = 9

            self.content['form'] = None  # message of correct
            return self.Render_HTML('root/sign_in.html')

        return self.Render_HTML('root/sign_in.html', 'login')

    def Manage_Form(self):

        if self.request.POST['__form__'] == 'login':
            return self.Manage_Form_Login()

        return Dynamic_Event_Manager.Manage_Form(self)

    @staticmethod
    def Redirect(request, url):
        other_value = {'redirect': url}
        return Sign_In(request, other_value=other_value,
                       length_navigation=2).HTML

    @staticmethod
    def Launch(request):
        return Sign_In(request).HTML



class Sign_Out(Dynamic_Event_Manager):

    def Manage_Content_Ground(self):
        self.request.session['root_login'] = False
        self.request.session['main_number_product_on_page'] = 10
        return self.Render_HTML('root/sign_out.html')

    def Check_Authorization(self):

        if self.authorization:
            if self.request.session['root_login']:
                return True

        else: return True
        return False

    @staticmethod
    def Launch(request):
        return Sign_Out(request, only_root=True).HTML



class Company_Details_Manager(Dynamic_Event_Manager):

    def Manage_Content_Ground(self):
        address = Root_Address.objects.first()
        self.content['form'] = Form_Root_Address(self.request, instance=address)
        return self.Render_HTML('root/company_details.html', 'root_address')

    def Manage_Form_Root_Address(self):

        address = Root_Address.objects.first()
        self.content['form'] = Form_Root_Address(self.request,
             self.request.POST, instance=address)

        if self.content['form'].is_valid():
            self.content['form'].save() # save change of address_user

            return self.Render_HTML('root/company_details.html', 'root_address')
        return self.Render_HTML('root/company_details.html', 'root_address')

    def Manage_Form(self):

        if self.request.POST['__form__'] == 'root_address':
            return self.Manage_Form_Root_Address()

        return Dynamic_Event_Manager.Manage_Form(self)

    @staticmethod
    def Launch(request):
        return Company_Details_Manager(request, only_root=True).HTML



class Users_Payments(Dynamic_Event_Manager):

    def Get_Date(self):

        date_from = self.request.session['root_users_payments_date_from']
        date_from = datetime.strptime(date_from, '%Y-%m-%d')
        date_to = self.request.session['root_users_payments_date_to']
        date_to = datetime.strptime(date_to, '%Y-%m-%d')

        return date_from, date_to

    def Create_Payment_Structure(self):

        self.content['shopping'] = []

        date_from, date_to = self.Get_Date()
        status = self.request.session['root_payment_status']
        payments = Payment.objects.filter(status=status,
                      date__gte=date_from, date__lte=date_to)

        for payment in payments:

            details = {
                'fullname': Invoice_Address.objects.get(payment=payment).full_name,
                'payment':  payment,
                'products': Selected_Product.objects.filter(payment=payment)
            }

            self.content['shopping'].append(details)

    def Manage_Content_Ground(self):
        self.Create_Payment_Structure()
        self.content['date_from'] = self.request.session['root_users_payments_date_from']
        self.content['date_to'] = self.request.session['root_users_payments_date_to']
        self.content['button_address_name'] = 'root_address'
        return self.Render_HTML('root/users_payments.html')

    def Manage_Button(self):

        if self.request.POST['__button__'] == 'assign':
            index = self.Get_Post_Value('index')
            payment = Payment.objects.get(pk=index)
            payment.status = self.request.POST['value']
            payment.save()

        if self.request.POST['__button__'] == 'change':
            self.request.session['root_payment_status'] = \
                self.request.POST['value']

        return JsonResponse({'__button__': 'true'})

    def Manage_Filter(self):

        if self.request.POST['__filter__'] == 'date_to':
            self.request.session['root_users_payments_date_to'] = \
                self.request.POST['value']

        if self.request.POST['__filter__'] == 'date_from':
            self.request.session['root_users_payments_date_from'] = \
                self.request.POST['value']

        self.Validate_Period('root_users_payments_date_from', 'root_users_payments_date_to')
        return JsonResponse({'__filter__': 'true'})

    def Manage_Form_Note(self):

        note = self.request.session['root_note']
        form_note = Form_Order_Note(self.request,
            self.request.POST)

        if form_note.is_valid():
            note.note = form_note.cleaned_data['note']
            note.save()

            note.Save_File(form_note.cleaned_data['file'])

            return Dialog_Prompt(self.request, self.app_name, apply=True).HTML
        return Dialog_Prompt(self.request, self.app_name, not_valid=True).HTML

    def Manage_Form_Deadline(self):

        note = self.request.session['root_deadline']
        form_deadline = Form_Order_Deadline(self.request,
            self.request.POST, instance=note)

        if form_deadline.is_valid():
            form_deadline.save()

            return Dialog_Prompt(self.request, self.app_name, apply=True).HTML
        return Dialog_Prompt(self.request, self.app_name, not_valid=True).HTML

    def Manage_Form(self):

        if self.request.POST['__form__'] == 'note':
            return self.Manage_Form_Note()

        if self.request.POST['__form__'] == 'deadline':
            return self.Manage_Form_Deadline()

        return Dynamic_Event_Manager.Manage_Form(self)

    @staticmethod
    def Launch(request):
        return Users_Payments(request, only_root=True).HTML



class Social_Media_Manager(Dynamic_Event_Manager):

    def Manage_Content_Ground(self):
        self.content['social_media'] = Social_Media.objects.all()
        return self.Render_HTML('root/social_media.html')

    def Manage_Form(self):

        pk = self.request.POST['__form__']
        url = self.request.POST['value']

        social = Social_Media.objects.get(pk=pk)
        social.url = url
        social.save()

        return JsonResponse({'__form__': 'true'})

    @staticmethod
    def Launch(request):
        return Social_Media_Manager(request, only_root=True).HTML



class Delivery_Settings(Dynamic_Event_Manager):

    def Manage_Content_Ground(self):
        self.content['options'] = Delivery.objects.all()
        return self.Render_HTML('root/delivery_settings.html')

    def Manage_Form(self):

        pk, currency = self.request.POST['__form__'].split(' ')
        price = float(self.request.POST['value']) * 100
        delivery = Delivery.objects.get(pk=pk)

        if currency == 'PLN':
            delivery.price_pln = price

        if currency == 'EUR':
            delivery.price_eur = price

        delivery.save()
        return JsonResponse({'__form__': 'true'})

    @staticmethod
    def Launch(request):
        return Delivery_Settings(request, only_root=True).HTML
