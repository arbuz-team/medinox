from server.manage.switch.website.manager import *
from server.manage.root.forms import *
from server.service.payment.models import *


class Panel_App(Website_Manager):

    def Manage_Content_Ground(self):

        path_manager = Path_Manager(self)
        self.content['apps'] = [
            {
                'name': Text(self, 24),
                'url': path_manager.Get_Path('root.sign_out', current_language=True),
                'icon': '/static/img/icons/128/dark/logout.png',
            },
            {
                'name': Text(self, 25),
                'url': path_manager.Get_Path('root.company_details', current_language=True),
                'icon': '/static/img/icons/128/dark/moustache.png',
            },
            {
                'name': Text(self, 27),
                'url': path_manager.Get_Path('root.users_payments', current_language=True),
                'icon': '/static/img/icons/128/dark/money.png',
            },
            {
                'name': Text(self, 135),
                'url': path_manager.Get_Path('root.social_media', current_language=True),
                'icon': '/static/img/icons/128/dark/social_group.png',
            },
            {
                'name': Text(self, 136),
                'url': path_manager.Get_Path('root.delivery_settings', current_language=True),
                'icon': '/static/img/icons/128/dark/transport.png',
            },
        ]

        return self.Render_HTML('arbuz/panel_app.html')

    @staticmethod
    def Launch(request):
        return Panel_App(request, only_root=True).HTML



class Sign_In(Website_Manager):

    def Manage_Content_Ground(self):
        self.content['form'] = Form_Root_Login(self)
        return self.Render_HTML('root/sign_in.html', 'login')

    def Manage_Form_Login(self):
        self.content['form'] = Form_Root_Login(self, post=True)

        if self.content['form'].is_valid():
            self.request.session['root_login'] = True
            self.request.session['main_number_product_on_page'] = 9

            self.content['form'] = None  # message of correct
            return self.Render_HTML('root/sign_in.html')

        return self.Render_HTML('root/sign_in.html', 'login')

    def Manage_Form(self):

        if self.request.POST['__form__'] == 'login':
            return self.Manage_Form_Login()

        return Website_Manager.Manage_Form(self)

    @staticmethod
    def Redirect(request, url):
        other_value = {'redirect': url}
        return Sign_In(request, other_value=other_value,
                       length_navigation=2).HTML

    @staticmethod
    def Launch(request):
        return Sign_In(request).HTML



class Sign_Out(Website_Manager):

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



class Company_Details_Manager(Website_Manager):

    def Manage_Content_Ground(self):
        address = SQL.First(Root_Address)
        self.content['form'] = Form_Root_Address(self, instance=address)
        return self.Render_HTML('root/company_details.html', 'root_address')

    def Manage_Form_Root_Address(self):

        address = SQL.First(Root_Address)
        self.content['form'] = Form_Root_Address(
            self, post=True, instance=address)

        if self.content['form'].is_valid():
            address = self.content['form'].save(commit=False) # save change of address_user
            SQL.Save(data=address)

            return self.Render_HTML('root/company_details.html', 'root_address')
        return self.Render_HTML('root/company_details.html', 'root_address')

    def Manage_Form(self):

        if self.request.POST['__form__'] == 'root_address':
            return self.Manage_Form_Root_Address()

        return Website_Manager.Manage_Form(self)

    @staticmethod
    def Launch(request):
        return Company_Details_Manager(request, only_root=True).HTML



class Users_Payments(Website_Manager):

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
        payments = SQL.Filter(Payment, status=status,
                      date__gte=date_from, date__lte=date_to)

        for payment in payments:

            details = {
                'fullname': SQL.Get(Invoice_Address, payment=payment).full_name,
                'payment':  payment,
                'products': SQL.Filter(Selected_Product, payment=payment)
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
            payment = SQL.Get(Payment, pk=index)
            payment.status = self.request.POST['value']
            SQL.Save(data=payment)

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
        form_note = Form_Order_Note(self, post=True)

        if form_note.is_valid():
            note.note = form_note.cleaned_data['note']
            SQL.Save(data=note)

            # save send files
            file = form_note.cleaned_data['file']
            file_name = form_note.cleaned_data['file_name']

            if file: # save if file was sent

                note_file = Note_File()
                note_file.note = note
                note_file.name = file_name
                SQL.Save(data=note_file)

                note_file.Save_File(file)

            return Dialog_Prompt(self.request, self.app_name, apply=True).HTML
        return Dialog_Prompt(self.request, self.app_name, not_valid=True).HTML

    def Manage_Form_Deadline(self):

        note = self.request.session['root_deadline']
        form_deadline = Form_Order_Deadline(self.request,
            self.request.POST, instance=note)

        if form_deadline.is_valid():
            SQL.Save(data=form_deadline)

            return Dialog_Prompt(self.request, self.app_name, apply=True).HTML
        return Dialog_Prompt(self.request, self.app_name, not_valid=True).HTML

    def Manage_Form(self):

        if self.request.POST['__form__'] == 'note':
            return self.Manage_Form_Note()

        if self.request.POST['__form__'] == 'deadline':
            return self.Manage_Form_Deadline()

        return Website_Manager.Manage_Form(self)

    @staticmethod
    def Launch(request):
        return Users_Payments(request, only_root=True).HTML



class Social_Media_Manager(Website_Manager):

    def Manage_Content_Ground(self):
        self.content['social_media'] = SQL.All(Social_Media)
        return self.Render_HTML('root/social_media.html')

    def Manage_Form(self):

        pk = self.request.POST['__form__']
        url = self.request.POST['value']

        social = SQL.Get(Social_Media, pk=pk)
        social.url = url
        SQL.Save(data=social)

        return JsonResponse({'__form__': 'true'})

    @staticmethod
    def Launch(request):
        return Social_Media_Manager(request, only_root=True).HTML



class Delivery_Settings(Website_Manager):

    def Manage_Content_Ground(self):
        self.content['options'] = SQL.All(Delivery)
        return self.Render_HTML('root/delivery_settings.html')

    def Manage_Form(self):

        pk, currency = self.request.POST['__form__'].split(' ')
        price = float(self.request.POST['value']) * 100
        delivery = SQL.Get(Delivery, pk=pk)

        if currency == 'PLN':
            delivery.price_pln = price

        if currency == 'EUR':
            delivery.price_eur = price

        SQL.Save(data=delivery)
        return JsonResponse({'__form__': 'true'})

    @staticmethod
    def Launch(request):
        return Delivery_Settings(request, only_root=True).HTML
