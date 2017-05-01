from payment.models import *
from user.models import *
from product.base import *


class Payment_Models_Manager(Dynamic_Base):

    def Count_Total_Price(self):

        selected_products = self.Get_Selected_Products()
        delivery = self.Get_Payment().delivery_price
        total = self.product_models_manager\
            .Get_Delivery_Price(delivery, current_currency=True)

        for selected in selected_products:
            product_price = self.product_models_manager\
                .Get_Product_Price(selected.product, current_currency=True)

            total += product_price * selected.number

        return format(total, '.2f')

    def Update_Total_Price(self):
        self.payment.total_price = self.Count_Total_Price()
        self.payment.save()

    def Check_Delivery_Address(self):

        payments_address = Delivery_Address.objects.filter(
            payment=self.payment)

        if payments_address.count() > 1:
            payments_address.delete()

        if not payments_address:
            Delivery_Address(
                full_name='',
                address_line='',
                city='',
                region='',
                postcode='',
                country='',
                payment=self.payment
            ).save()

    def Check_Invoice_Address(self):

        invoice_address = Invoice_Address.objects.filter(
            payment=self.payment)

        if invoice_address.count() > 1:
            invoice_address.delete()

        if not invoice_address:
            Invoice_Address(
                full_name='',
                address_line='',
                city='',
                region='',
                postcode='',
                country='',
                payment=self.payment
            ).save()

    def Check_Payment(self):

        if not self.request.session['user_unique']:
            return

        unique = self.request.session['user_unique']
        self.user = User.objects.get(unique=unique)

        payments = Payment.objects.filter(user=self.user, approved=False)
        if payments.count() > 1:
            payments.delete()

        if not payments:

            # delivery prices for first user address
            address = User_Address.objects.first()
            delivery = Delivery.objects.get(country=address.country)

            payment = Payment(
                user=self.user,
                date=date.today(),
                total_price='0.00',
                delivery_price=delivery,
                service='None',
                currency=self.request.session['translator_currency']
            )
            payment.save()

        self.payment = Payment.objects.get(user=self.user, approved=False)
        self.Check_Delivery_Address()
        self.Check_Invoice_Address()

    def Get_Selected_Products(self):
        return Selected_Product.objects.filter(payment=self.payment)

    def Get_Payment(self):
        return Payment.objects.get(user=self.user, approved=False)

    def Append_Selected_Product(self, product):
        selected_product = Selected_Product.objects.filter(
            payment=self.payment, product=product)

        # append new product
        if not selected_product:

            Selected_Product(
                payment=self.payment,
                product=product,
                number=1
            ).save()

    def Delete_Selected_Product(self, product):
        selected_product = Selected_Product.objects.get(
            payment=self.payment, product=product)

        selected_product.delete()

    def Clear_Selected_Product(self):
        Selected_Product.objects.filter(payment=self.payment).delete()

    def Edit_Number_Of_Products(self, selected_pk, number):
        selected_product = Selected_Product.objects.get(
            pk=selected_pk)

        selected_product.number = number
        selected_product.save()

    def __init__(self, request):
        Dynamic_Base.__init__(self, request)

        self.user = None
        self.payment = None
        self.product_models_manager = \
            Product_Models_Manager(self.request)

        self.Check_Payment()
