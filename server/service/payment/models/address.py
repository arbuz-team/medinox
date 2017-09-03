from .payment import *


class Delivery_Address(Abstract_Address):

    payment = models.OneToOneField(Payment)

    @staticmethod
    def Initialize(payment):

        payments_address = SQL.Filter(
            Delivery_Address, payment=payment)

        if payments_address.count() > 1:
            SQL.Delete(data=payments_address)

        if not payments_address:
            SQL.Save(Delivery_Address,
                full_name='',
                address_line='',
                city='',
                region='',
                postcode='',
                country='',
                payment=payment
            )



class Invoice_Address(Abstract_Address):

    payment = models.OneToOneField(Payment)

    @staticmethod
    def Initialize(payment):

        invoice_address = SQL.Filter(
            Invoice_Address, payment=payment)

        if invoice_address.count() > 1:
            SQL.Delete(data=invoice_address)

        if not invoice_address:
            SQL.Save(Invoice_Address,
                full_name='',
                address_line='',
                city='',
                region='',
                postcode='',
                country='',
                payment=payment
            )
