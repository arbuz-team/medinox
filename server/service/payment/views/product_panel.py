from server.manage.switch.website import *


class Buy(Website_Manager):

    def Manage_Form(self):
        product = SQL.Get(Product, pk=self.other_value)
        self.payment_models_manager.Add_Cart_Product(product)

        path_manager = Path_Manager(self)
        url = path_manager.Get_Path('payment', current_language=True)
        return HttpResponseRedirect(url)

    @staticmethod
    def Launch(request, pk):
        return Buy(request, other_value=pk).HTML



class Cart_Manager(Website_Manager):

    def Manage_Form(self):
        product = SQL.Get(Product, pk=self.other_value)
        self.payment_models_manager.Add_Cart_Product(product)
        return HttpResponse()

    @staticmethod
    def Launch(request, pk):
        return Cart_Manager(request, other_value=pk).HTML
