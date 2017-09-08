from server.service.payment.models import *
from server.manage.user.models import *
from server.manage.switch.website.base import *


class Payment_Models_Manager(Base_Website):

    # base cart operations

    def Get_Cart(self): # cart is not approved payment
        return SQL.Get(Model_Payment, user=self.user, status='cart')

    def Clear_Cart(self):
        SQL.Delete(Model_Payment_Product,
           payment=self.payment)



    # products in cart operations

    def Add_Cart_Product(self, product):
        selected_product = SQL.Filter(Model_Payment_Product,
            payment=self.payment, product=product)

        # append new product
        if not selected_product:

            # get widgets with values
            values = []
            for key in self.request.POST.keys():
                if 'widget_' in key:
                    values.append(self.request.POST[key])

            # create selected product
            selected_product = Model_Payment_Product(
                payment=self.payment,
                product=product,
                number=1
            )

            # add values
            SQL.Save(data=selected_product)
            selected_product.values.add(*values)

    def Delete_Cart_Product(self, product):
        SQL.Delete(Model_Payment_Product, payment=self.payment,
                   product=product)

    @staticmethod
    def Edit_Number_Of_Cart_Products(selected_pk, number):
        selected_product = SQL.Get(
            Model_Payment_Product, pk=selected_pk)

        selected_product.number = number
        SQL.Save(data=selected_product)



    # initializate method

    def Initialize_Cart(self):

        self.user = self.request.session['user_user']
        if not self.user:
            return

        Model_Payment.Initialize(self, self.user)
        self.payment = SQL.Get(Model_Payment,
                user=self.user, status='cart')

        Model_Delivery_Address.Initialize(self.payment)
        Model_Invoice_Address.Initialize(self.payment)
        Model_Order_Deadline.Initialize(self.payment)
        Model_Order_Note.Initialize(self.payment)

    def __init__(self, _object):
        Base_Website.__init__(self, _object)

        self.user = None
        self.payment = None
        self.Initialize_Cart()
