from server.manage.switch.website.manager import *
from server.service.payment.base import *


class Cart_Manager(Website_Manager):

    def Manage_Content_Ground(self):
        pass

    def Manage_Content_Cart(self):

        self.content['payment'] = self.payment_models_manager.\
            Get_Payment()

        self.content['cart'] = self.payment_models_manager.\
            Get_Selected_Products()

        return self.Render_HTML('cart/cart.html')

    def Manage_Content(self):

        if self.request.POST['__content__'] == 'cart':
            return self.Manage_Content_Cart()

        return Website_Manager.Manage_Content(self)

    def Manage_Button_Append(self):
        product = SQL.Get(Product, pk=self.request.POST['value'])
        self.payment_models_manager.Append_Selected_Product(product)
        return JsonResponse({'__button__': 'true'})

    def Manage_Button_Delete(self):
        product = SQL.Get(Product, pk=self.request.POST['value'])
        self.payment_models_manager.Delete_Selected_Product(product)
        return JsonResponse({'__button__': 'true'})

    def Manage_Button_Clear(self):
        self.payment_models_manager.Clear_Selected_Product()
        return JsonResponse({'__button__': 'true'})

    def Manage_Button(self):
        return_value = None

        if self.request.POST['__button__'] == 'append':
            return_value = self.Manage_Button_Append()

        if self.request.POST['__button__'] == 'delete':
            return_value = self.Manage_Button_Delete()

        if self.request.POST['__button__'] == 'clear':
            return_value = self.Manage_Button_Clear()

        self.payment_models_manager.Update_Total_Price()
        return return_value

    def Manage_Little_Form(self):

        selected_pk = self.request.POST['__little__']
        number = self.request.POST['value']

        self.payment_models_manager.Edit_Number_Of_Products(
            selected_pk, number)

        return JsonResponse({'__button__': 'true'})

    @staticmethod
    def Launch(request):
        return Cart_Manager(request, authorization=True).HTML
