from server.service.payment.models import *
from server.manage.user.models import *
from server.manage.switch.website.base import *


class Payment_Models_Manager(Base_Website):

    # base cart operations

    def Get_Cart(self): # cart is not approved payment
        return SQL.Get(Payment, user=self.user, status='cart')

    def Clear_Cart(self):
        SQL.Delete(Payment_Product,
           payment=self.payment, force=True)



    # products in cart operations

    def Add_Cart_Product(self, product):
        selected_product = SQL.Filter(Payment_Product,
            payment=self.payment, product=product)

        # append new product
        if not selected_product:

            # get widgets with values
            values = []
            for key in self.request.POST.keys():
                if 'widget_' in key:
                    values.append(self.request.POST[key])

            # create selected product
            selected_product = Payment_Product(
                payment=self.payment,
                product=product,
                number=1
            )

            # add values
            SQL.Save(data=selected_product)
            selected_product.values.add(*values)

    def Delete_Cart_Product(self, product):
        SQL.Delete(Payment_Product, payment=self.payment,
                   product=product, force=True)

    @staticmethod
    def Edit_Number_Of_Cart_Products(selected_pk, number):
        selected_product = SQL.Get(
            Payment_Product, pk=selected_pk)

        selected_product.number = number
        SQL.Save(data=selected_product)



    # initializate method

    def Initialize_Cart(self):

        self.user = self.request.session['user_user']
        if not self.user:
            return

        Payment.Initialize(self, self.user)
        self.payment = SQL.Get(Payment,
                user=self.user, status='cart')

        Delivery_Address.Initialize(self.payment)
        Invoice_Address.Initialize(self.payment)
        Order_Deadline.Initialize(self.payment)
        Order_Note.Initialize(self.payment)

    def __init__(self, _object):
        Base_Website.__init__(self, _object)

        self.user = None
        self.payment = None
        self.Initialize_Cart()
