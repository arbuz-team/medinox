from .payment import *


class Model_Delivery_Address(Abstract_Address):

    payment = models.OneToOneField(Model_Payment)

    @staticmethod
    def Initialize(payment):

        payments_address = SQL.Filter(
            Model_Delivery_Address, payment=payment)

        if payments_address.count() > 1:
            SQL.Delete(data=payments_address)

        if not payments_address:
            SQL.Save(Model_Delivery_Address,
                name='',
                surname='',
                company_name='',
                nip='',
                address_line='',
                city='',
                region='',
                postcode='',
                country='',
                payment=payment
            )



class Model_Invoice_Address(Abstract_Address):

    payment = models.OneToOneField(Model_Payment)

    @staticmethod
    def Initialize(payment):

        invoice_address = SQL.Filter(
            Model_Invoice_Address, payment=payment)

        if invoice_address.count() > 1:
            SQL.Delete(data=invoice_address)

        if not invoice_address:
            SQL.Save(Model_Invoice_Address,
                name='',
                surname='',
                company_name='',
                nip='',
                address_line='',
                city='',
                region='',
                postcode='',
                country='',
                payment=payment
            )
