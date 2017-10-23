from server.manage.switch.templatetags.base import *
from server.service.currency.views.base import *


class Finance_Manager(Base_Tag_Manager):

    @staticmethod
    @register.simple_tag(takes_context=True)
    def get_price(context, product):
        currency = context.request.session['currency_selected']
        if not product.price:
            price = 0
        else:

            currency_manager = Base_Currency_Manager(context)
            price = currency_manager.Get_Price(product.price)

        return '{0:.2f} {1}'.format(price, currency)

    @staticmethod
    @register.simple_tag(takes_context=True)
    def get_widget_price(context, widget):
        currency = context.request.session['currency_selected']
        if not widget.super_price:
            price = 0
        else:

            currency_manager = Base_Currency_Manager(context)
            price = currency_manager.Get_Price(widget.super_price)

        return '{0:.2f} {1}'.format(price, currency)

    @staticmethod
    @register.simple_tag
    def price(price, currency):
        price = float(price)
        if not price: price = 0
        return '{0:.2f} {1}'.format(price, currency)

    @staticmethod
    @register.simple_tag
    def netto_price(price, currency, _vat=23):
        price = float(price)
        if not price: price = 0
        else: price -= price * _vat / (100 + _vat)
        return '{0:.2f} {1}'.format(price, currency)

    @staticmethod
    @register.simple_tag()
    def vat_price(price, currency, _vat=23):
        price = float(price)
        if not price: price = 0
        else: price = price * _vat / (100 + _vat)
        return '{0:.2f} {1}'.format(price, currency)
