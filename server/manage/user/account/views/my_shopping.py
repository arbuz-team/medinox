from server.manage.switch.website.manager import *
from server.manage.user.account.forms import *
from server.service.payment.models import *


class My_Shopping(Website_Manager):

    def Get_Date(self):

        date_from = self.request.session['user_my_shopping_date_from']
        date_from = datetime.strptime(date_from, '%Y-%m-%d')
        date_to = self.request.session['user_my_shopping_date_to']
        date_to = datetime.strptime(date_to, '%Y-%m-%d')

        return date_from, date_to

    def Create_Payment_Structure(self):

        self.context['shopping'] = []

        date_from, date_to = self.Get_Date()
        user = self.request.session['user_user']
        payments = SQL.Filter(Model_Payment, user=user, status='cart',
                              date__gte=date_from, date__lte=date_to)

        for payment in payments:

            details = {
                'payment': payment,
                'name': SQL.Get(Model_Delivery_Address, payment=payment).name,
                'surname': SQL.Get(Model_Delivery_Address, payment=payment).nazwisko,
                'company_name': SQL.Get(Model_Delivery_Address, payment=payment).company_name,
                'products': SQL.Filter(Model_Payment_Product, payment=payment)
            }

            self.context['shopping'].append(details)

    def Manage_Content(self):
        self.Create_Payment_Structure()
        self.context['date_from'] = self.request.session['user_my_shopping_date_from']
        self.context['date_to'] = self.request.session['user_my_shopping_date_to']
        self.context['button_address_name'] = 'user_address'
        return self.Render_HTML('user/account/my_shopping.html')

    def Manage_Filter(self):

        if self.request.POST['_name_'] == 'date_to':
            self.request.session['user_my_shopping_date_to'] = \
                self.request.POST['value']

        if self.request.POST['_name_'] == 'date_from':
            self.request.session['user_my_shopping_date_from'] = \
                self.request.POST['value']

        self.Validate_Period('user_my_shopping_date_from', 'user_my_shopping_date_to')
        return HttpResponse()

    @staticmethod
    def Launch(request):
        return My_Shopping(request, authorization=True).HTML



class Selected_Shopping(Website_Manager):

    def Create_Payment_Structure(self):
        payment = SQL.Get(Model_Payment, unique=self.other_value)

        self.context['shopping'] = [{
            'name': SQL.Get(Model_Invoice_Address, payment=payment).name,
            'surname': SQL.Get(Model_Invoice_Address, payment=payment).surname,
            'company_name': SQL.Get(Model_Invoice_Address, payment=payment).company_name,
            'payment':  payment,
            'products': SQL.Filter(Model_Payment_Product, payment=payment)
        }]

    def Manage_Content(self):
        self.Create_Payment_Structure()
        self.context['button_address_name'] = 'user_address'
        return self.Render_HTML('user/account/my_shopping.html')

    @staticmethod
    def Launch(request, unique):
        return Selected_Shopping(request,
             authorization=True, other_value=unique).HTML
