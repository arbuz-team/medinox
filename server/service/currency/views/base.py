from server.service.translator.views import *


class Base_Currency_Manager(Base):

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
