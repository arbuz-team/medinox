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
        html = fp.read().decode("utf8")
        fp.close()

        # parse html
        html = html[html.find('span'):html.rfind('span')]
        price = html[html.find('>'):html.rfind('<')]

        return price

    def Manage_Get(self):

        if self.request.POST['_name_'] == 'exchange_rate':
            amount = self.request.POST['amount']
            currency_from = self.request.POST['currency_from']
            currency_to = self.request.POST['currency_to']
            return self.Exchange_Rate(amount, currency_from, currency_to)

    def Manage_Button(self):

        selected_currency = self.request.POST['value']
        if selected_currency in ['PLN', 'EUR', 'GBP']:
            self.request.session['language_currency'] = \
                selected_currency

        return HttpResponse()

    @staticmethod
    def Launch(request):
        return Currency_Manager(request).HTML
