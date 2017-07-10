from server.manage.switch.website.base import *


class Product_Models_Manager(Base_Website):

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
        Base_Website.__init__(self, request)
