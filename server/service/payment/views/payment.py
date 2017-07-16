from .dotpay import *
from .paypal import *


class Payment_Manager(Website_Manager, PayPal, DotPay):

    def Update_Payment(self):

        payment = SQL.Get(Payment,
            user=self.content['user'], status='cart')

        self.content['payment'] = payment.pk
        payment.date = datetime.today().date()
        payment.total_price = self.content['total_price']
        payment.currency = self.request.session['translator_currency']
        SQL.Save(data=payment)

    def Load_Payment_Details(self):

        model_manager = Payment_Models_Manager(self)
        self.content['user'] = self.request.session['user_user']
        self.content['cart'] = model_manager.Get_Selected_Products()
        self.content['total_price'] = model_manager.Count_Total_Price()
        self.content['delivery'] = model_manager.Get_Payment().delivery_price
        self.content['address'] = SQL.Filter(User_Address, user=self.content['user'])
        self.Update_Payment()

        self.content['paypal'] = self.Create_PayPal_From()
        self.content['dotpay'] = self.Create_DotPay_From()

    def Create_Address(self, pk, model):

        user_address = SQL.Get(User_Address, pk=pk)
        address = None

        user = self.request.session['user_user']
        payment = SQL.Get(Payment, user=user, status='cart')

        if model == 'delivery_address':
            address = SQL.Get(Delivery_Address, payment=payment)

        if model == 'invoice_address':
            address = SQL.Get(Invoice_Address, payment=payment)

        address.full_name = user_address.full_name
        address.address_line = user_address.address_line
        address.city = user_address.city
        address.region = user_address.region
        address.postcode = user_address.postcode
        address.country = user_address.country
        SQL.Save(data=address)

    def Manage_Content_Ground(self):
        self.Load_Payment_Details()
        return self.Render_HTML('payment/payment.html')


    def Manage_Form_Address_Payment(self):

        address_payment_pk = self.request.POST['shipment']
        address_invoice_pk = self.request.POST['invoice']

        self.Create_Address(address_payment_pk, 'delivery_address')
        self.Create_Address(address_invoice_pk, 'invoice_address')

        self.Load_Payment_Details()
        self.content['address_is_validate'] = True
        return self.Render_HTML('payment/payment.html')

    def Manage_Form(self):

        if self.request.POST['__form__'] == 'address':
            return self.Manage_Form_Address_Payment()

        return Website_Manager.Manage_Form(self)


    def Manage_Get_Delivery(self):

        address = SQL.Get(User_Address, pk=self.request.POST['value'])
        delivery = SQL.Get(Delivery, country=address.country)
        user = self.request.session['user_user']
        payment = SQL.Get(Payment, user=user, status='cart')

        payment.delivery_price = delivery
        SQL.Save(data=payment)

        prices = {
            'eur': delivery.price_eur,
            'pln': delivery.price_pln,
        }

        return JsonResponse(prices)

    def Manage_Get(self):

        if self.request.POST['__get__'] == 'delivery':
            self.Manage_Get_Delivery()

        return Website_Manager.Manage_Get(self)

    @staticmethod
    def Launch(request):
        return Payment_Manager(request, authorization=True).HTML



class Apply_Payment(Website_Manager):

    def Manage_Content_Ground(self):
        return self.Render_HTML('payment/apply.html')

    def Error_No_Event(self):
        return self.Manage_Index()

    @staticmethod
    @csrf_exempt
    def Launch(request):
        return Apply_Payment(request).HTML



class Cancel_Payment(Website_Manager):

    def Manage_Content_Ground(self):
        return self.Render_HTML('payment/cancel.html')

    def Error_No_Event(self):
        return self.Manage_Index()

    @staticmethod
    @csrf_exempt
    def Launch(request):
        return Cancel_Payment(request).HTML



class Buy(Website_Manager):

    def Manage_Form(self):
        product = SQL.Get(Product, pk=self.other_value)
        self.payment_models_manager.Append_Selected_Product(product)
        return self.Render_HTML('payment/buy.html')

    @staticmethod
    def Buy_Product(request, pk):
        return Buy(request, other_value=pk).HTML

    @staticmethod
    def Launch(request):
        return Buy(request).HTML
