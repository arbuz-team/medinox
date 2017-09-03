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
        payments = SQL.Filter(Payment, user=user, status='cart',
                              date__gte=date_from, date__lte=date_to)

        for payment in payments:

            details = {
                'payment': payment,
                'full_name': SQL.Get(Delivery_Address, payment=payment).full_name,
                'products': SQL.Filter(Payment_Product, payment=payment)
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
