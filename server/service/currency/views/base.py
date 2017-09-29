from server.service.translator.views import *


class Base_Currency_Manager(Base):

    def Exchange_Rate(self, amount, currency_to):

        path_manager = Path_Manager(self)
        path = path_manager.Base_Root(
            'server/manage/setting/data/_exchange_rate')

        price = 0
        file = open(path)
        content = file.read().splitlines()

        for line in content:
            if currency_to in line:
                rate = float(line.split(':')[1])
                price = float(amount) * rate

        return '{0:.2f}'.format(price)

    def Get_Price(self, price):
        price_pln = price

        switch = {
            'PLN': price_pln,
            'EUR': self.Exchange_Rate(price_pln, 'EUR'),
            'GBP': self.Exchange_Rate(price_pln, 'GBP'),
        }

        currency = self.request.session['currency_selected']
        return float(switch[currency])

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
