from server.manage.switch.website.manager import *
from server.service.searcher.payment import *


class Search_Payments(Website_Manager):

    def Get_Date(self):

        date_from = self.request.session['root_users_payments_date_from']
        date_from = datetime.strptime(date_from, '%Y-%m-%d')
        date_to = self.request.session['root_users_payments_date_to']
        date_to = datetime.strptime(date_to, '%Y-%m-%d')

        return date_from, date_to

    def Set_Date(self):

        if 'date_to' in self.request.POST:
            self.request.session['root_users_payments_date_to'] = \
                self.request.POST['date_to']

        if 'date_from' in self.request.POST:
            self.request.session['root_users_payments_date_from'] = \
                self.request.POST['date_from']

        self.Validate_Period('root_users_payments_date_from',
                             'root_users_payments_date_to')

    def Manage_Content(self):
        self.context['date_from'] = self.request.session['root_users_payments_date_from']
        self.context['date_to'] = self.request.session['root_users_payments_date_to']
        self.context['button_address_name'] = 'root_address'
        return self.Render_HTML('root/search_payments.html')

    def Manage_Form_Searcher(self):

        phrase = self.request.POST['phrase']
        engine = Search_Engine(self, phrase)

        self.context['shopping'] = []
        self.context['phrase'] = phrase
        self.Set_Date()

        date_from, date_to = self.Get_Date()
        payments = engine.Search_Payments()
        payments = SQL.Filter(Model_Payment, pk__in=payments,
                              date__gte=date_from, date__lte=date_to)

        for payment in payments:

            details = {
                'name': SQL.Get(Model_Invoice_Address, payment=payment).name,
                'surname': SQL.Get(Model_Invoice_Address, payment=payment).surname,
                'company_name': SQL.Get(Model_Invoice_Address, payment=payment).company_name,
                'payment':  payment,
                'products': SQL.Filter(Model_Payment_Product, payment=payment)
            }

            self.context['shopping'].append(details)

        return self.Manage_Content()

    def Manage_Form(self):

        if self.request.POST['_name_'] == 'searcher':
            return self.Manage_Form_Searcher()

    @staticmethod
    def Launch(request):
        return Search_Payments(request, only_root=True).HTML
