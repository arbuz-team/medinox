from server.manage.switch.website.endpoints import *
from server.manage.switch.website.inspector import *
from server.service.payment.base import *


class Cart_Block(Endpoints, Inspector):

    def Manage_Content(self):

        # check authorization
        if not self.Check_Authorization():
            return HttpResponse()

        payment = self.payment_models_manager.Get_Cart()

        self.context['payment'] = payment
        self.context['cart'] = SQL.Filter(
            Payment_Product, payment=payment)

        return self.Render_HTML('block/cart.html')

    def Manage_Button_Append(self):
        product = SQL.Get(Product, pk=self.request.POST['value'])
        self.payment_models_manager.Add_Cart_Product(product)
        return HttpResponse()

    def Manage_Button_Delete(self):
        product = SQL.Get(Product, pk=self.request.POST['value'])
        self.payment_models_manager.Delete_Cart_Product(product)
        return HttpResponse()

    def Manage_Button_Clear(self):
        self.payment_models_manager.Clear_Cart()
        return HttpResponse()

    def Manage_Button(self):
        return_value = None

        if self.request.POST['_name_'] == 'append':
            return_value = self.Manage_Button_Append()

        if self.request.POST['_name_'] == 'delete':
            return_value = self.Manage_Button_Delete()

        if self.request.POST['_name_'] == 'clear':
            return_value = self.Manage_Button_Clear()

        cart = self.payment_models_manager.Get_Cart()
        cart.Update_Total_Price(self)
        return return_value

    def Manage_Little_Form(self):

        selected_pk = self.request.POST['__little__']
        number = self.request.POST['value']

        self.payment_models_manager\
            .Edit_Number_Of_Cart_Products(selected_pk, number)

        return HttpResponse()

    def Error(self, response_class, context):
        return response_class(self.Render_To_String(
            'error/cart.html', context=context))

    def __init__(self, _object):
        Endpoints.__init__(self, _object)
        Inspector.__init__(self, _object)

        self.authorization = True
        self.payment_models_manager = \
            Payment_Models_Manager(self)

