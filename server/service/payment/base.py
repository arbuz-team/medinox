from server.service.payment.models import *
from server.manage.user.models import *
from server.manage.switch.website.base import *


class Payment_Models_Manager(Base_Website):

    def Count_Total_Price(self):

        selected_products = self.Get_Selected_Products()
        delivery = self.Get_Payment().delivery_price
        total = delivery.price_eur

        for selected in selected_products:
            product_price = selected.price

            total += product_price * selected.number

        return format(total, '.2f')

    def Update_Total_Price(self):
        self.payment.total_price = self.Count_Total_Price()
        SQL.Save(data=self.payment)

    def Check_Delivery_Address(self):

        payments_address = SQL.Filter(
            Delivery_Address, payment=self.payment)

        if payments_address.count() > 1:
            payments_address.delete()

        if not payments_address:
            SQL.Save(Delivery_Address,
                full_name='',
                address_line='',
                city='',
                region='',
                postcode='',
                country='',
                payment=self.payment
            )

    def Check_Invoice_Address(self):

        invoice_address = SQL.Filter(
            Invoice_Address, payment=self.payment)

        if invoice_address.count() > 1:
            invoice_address.delete()

        if not invoice_address:
            SQL.Save(Invoice_Address,
                full_name='',
                address_line='',
                city='',
                region='',
                postcode='',
                country='',
                payment=self.payment
            )

    def Check_Order_Note(self):

        order_notes = SQL.Filter(
            Order_Note, payment=self.payment)

        if order_notes.count() > 1:
            order_notes.delete()

        if not order_notes:
            SQL.Save(Order_Note,
                note='',
                payment=self.payment
            )

    def Check_Order_Deadline(self):

        order_deadline = SQL.Filter(
            Order_Deadline, payment=self.payment)

        if order_deadline.count() > 1:
            order_deadline.delete()

        if not order_deadline:
            SQL.Save(Order_Deadline,
                name='',
                send_to_buyer=False,
                send_to_root=False,
                payment=self.payment
            )

    def Check_Payment(self):

        if not self.request.session['user_user']:
            return

        self.user = self.request.session['user_user']
        payments = SQL.Filter(Payment, user=self.user, status='cart')

        if payments.count() > 1:
            payments.delete()

        if not payments:

            # delivery prices for first user address
            address = SQL.First(User_Address)
            delivery = SQL.Get(Delivery, country=address.country)

            payment = Payment(
                user=self.user,
                date=datetime.today().date(),
                total_price='0.00',
                delivery_price=delivery,
                service='None',
                currency=self.request.session['translator_currency'],
                status='cart'
            )
            SQL.Save(data=payment)

        self.payment = SQL.Get(Payment, user=self.user, status='cart')
        self.Check_Delivery_Address()
        self.Check_Invoice_Address()
        self.Check_Order_Deadline()
        self.Check_Order_Note()

    def Get_Selected_Products(self):
        return SQL.Filter(Selected_Product, payment=self.payment)

    def Get_Payment(self):
        return SQL.Get(Payment, user=self.user, status='cart')

    def Append_Selected_Product(self, product):
        selected_product = SQL.Filter(Selected_Product,
            payment=self.payment, product=product)

        # append new product
        if not selected_product:

            # get widgets with values
            values = []
            for key in self.request.POST.keys():
                if 'widget_' in key:
                    values.append(self.request.POST[key])

            # create selected product
            selected_product = Selected_Product(
                payment=self.payment,
                product=product,
                number=1
            )

            # add values
            SQL.Save(data=selected_product)
            selected_product.values.add(*values)

    def Delete_Selected_Product(self, product):
        selected_product = SQL.Get(Selected_Product,
            payment=self.payment, product=product)

        selected_product.delete()

    def Clear_Selected_Product(self):
        SQL.Filter(Selected_Product, payment=self.payment).delete()

    def Edit_Number_Of_Products(self, selected_pk, number):
        selected_product = SQL.Get(
            Selected_Product, pk=selected_pk)

        selected_product.number = number
        SQL.Save(data=selected_product)

    def __init__(self, _object):
        Base_Website.__init__(self, _object)

        self.user = None
        self.payment = None
        self.Check_Payment()
