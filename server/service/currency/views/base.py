from server.service.translator.views import *
import urllib.request


class Base_Currency_Manager(Base):

    @staticmethod
    def Exchange_Rate(amount, currency_from, currency_to):

        # create url
        url = 'https://finance.google.com/finance/converter?a={0}&from={1}&to={2}'
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

    def Set_Default_Currency(self):

        geo = GeoIP()
        client_ip = self.request.META.get('REMOTE_ADDR', None)
        country = geo.country_code(client_ip)

        if country == 'PL':
            self.request.session['currency_selected'] = 'PLN'

        if country == 'DE':
            self.request.session['currency_selected'] = 'EUR'

        if country == 'GB': # united kingdom
            self.request.session['currency_selected'] = 'GBP'
