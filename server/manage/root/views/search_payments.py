from server.manage.switch.website.manager import *
from server.service.searcher.payment import *


class Search_Payments(Website_Manager):

    def Manage_Content(self):
        return HttpResponse('SAM SE NAPISZ')

    def Manage_Form_Searcher(self):

        phrase = self.request.POST['phrase']
        engine = Search_Engine(self, phrase)
        payments = engine.Search_Payments()

        self.context['shopping'] = []
        self.context['phrase'] = phrase

        for payment in payments:

            details = {
                'fullname': SQL.Get(Model_Invoice_Address, payment=payment).full_name,
                'payment':  payment,
                'products': SQL.Filter(Model_Payment_Product, payment=payment)
            }

            self.context['shopping'].append(details)

        self.context['date_from'] = self.request.session['root_users_payments_date_from']
        self.context['date_to'] = self.request.session['root_users_payments_date_to']
        self.context['button_address_name'] = 'root_address'
        return self.Render_HTML('root/search_payments.html')

    def Manage_Form(self):

        if self.request.POST['_name_'] == 'searcher':
            return self.Manage_Form_Searcher()

    @staticmethod
    def Launch(request):
        return Search_Payments(request, only_root=True).HTML
