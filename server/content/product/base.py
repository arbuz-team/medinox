from server.manage.switch.base import *


class Product_Models_Manager(Dynamic_Base):

    def Get_Product_Name(self, product):

        # if self.request.session['translator_language'] == 'EN':
        #     return product.details_en.name
        #
        # if self.request.session['translator_language'] == 'PL':
        #     return product.details_pl.name
        #
        # if self.request.session['translator_language'] == 'DE':
        #     return product.details_de.name
        return ''

    def Get_Product_Description(self, product):

        # if self.request.session['translator_language'] == 'EN':
        #     return product.details_en.description
        #
        # if self.request.session['translator_language'] == 'PL':
        #     return product.details_pl.description
        #
        # if self.request.session['translator_language'] == 'DE':
        #     return product.details_de.description
        return ''

    def Get_Purpose_Name(self, purpose):

        # if self.request.session['translator_language'] == 'EN':
        #     return purpose.name_en
        #
        # if self.request.session['translator_language'] == 'PL':
        #     return purpose.name_pl
        #
        # if self.request.session['translator_language'] == 'DE':
        #     return purpose.name_de
        return ''

    def Get_Purposes_Names(self, product):

        # if self.request.session['translator_language'] == 'EN':
        #     return ' '.join(product.purpose.all().values_list('name_en', flat=True))
        #
        # if self.request.session['translator_language'] == 'PL':
        #     return ' '.join(product.purpose.all().values_list('name_pl', flat=True))
        #
        # if self.request.session['translator_language'] == 'DE':
        #     return ' '.join(product.purpose.all().values_list('name_de', flat=True))
        return ''

    def Get_Product_Price(self, product, currency=None,
                          current_currency=False):

        # prices = \
        # {
        #     'EUR': product.price_eur / 100,
        #     'PLN': product.price_pln / 100
        # }
        #
        # if currency:
        #     return prices[currency]
        #
        # if current_currency:
        #     return prices[self.request.session['translator_currency']]
        #
        # return prices
        return 0

    def Get_Delivery_Price(self, delivery, currency=None,
                           current_currency=False):

        # prices = \
        # {
        #     'EUR': delivery.price_eur / 100,
        #     'PLN': delivery.price_pln / 100
        # }
        #
        # if currency:
        #     return prices[currency]
        #
        # if current_currency:
        #     return prices[self.request.session['translator_currency']]
        #
        # return prices
        return 0

    def __init__(self, request):
        Dynamic_Base.__init__(self, request)
