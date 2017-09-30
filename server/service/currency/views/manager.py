from server.manage.switch.website import *
from .base import *


class Currency_Manager(Website_Manager, Base_Currency_Manager):

    def Manage_Get(self):

        if self.request.POST['_name_'] == 'exchange_rate':

            amount = self.request.POST['amount']
            currency_from = self.request.POST['currency_from']
            currencies_to = self.request.POST['currencies_to']
            currencies_to = currencies_to.split(' ')

            response = {}
            for currency_to in currencies_to:
                response[currency_to] = self.Exchange_Rate(
                    amount, currency_to)

            return JsonResponse(response)

    def Manage_Button(self):

        selected_currency = self.request.POST['value']
        if selected_currency in ['PLN', 'EUR', 'GBP']:
            self.request.session['currency_selected'] = \
                selected_currency

        return HttpResponse()

    @staticmethod
    def Launch(request):
        return Currency_Manager(request).HTML
