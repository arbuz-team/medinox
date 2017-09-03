from server.manage.switch.website import *
from .base import *
import urllib.request


class Currency_Manager(Website_Manager, Base_Currency_Manager):

    @staticmethod
    def Exchange_Rate(amount, currency_from, currency_to):

        # create url
        url = 'https://www.google.com/finance/converter?a={0}&from={1}&to={2}'
        url = url.format(amount, currency_from, currency_to)

        # get html
        fp = urllib.request.urlopen(url)
        html = fp.read().decode('ISO-8859-1')
        fp.close()

        # parse html
        html = html[html.find('span'):html.rfind('span')]
        price = html[html.find('>'):html.rfind('<')]
        price = float(price[1:-4])

        return '{0:.2f}'.format(price)

    def Manage_Get(self):

        if self.request.POST['_name_'] == 'exchange_rate':

            amount = self.request.POST['amount']
            currency_from = self.request.POST['currency_from']
            currencies_to = self.request.POST['currencies_to']
            currencies_to = currencies_to.split(' ')

            response = {}
            for currency_to in currencies_to:
                response[currency_to] = self.Exchange_Rate(
                    amount, currency_from, currency_to)

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
