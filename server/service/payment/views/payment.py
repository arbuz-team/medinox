from server.service.payment.views.payment_method.dotpay import *
from server.service.payment.views.payment_method.paypal import *


class Payment_Manager(Website_Manager):

    def Update_Payment(self):

        payment = SQL.Get(Model_Payment,
            user=self.context['user'], status='cart')

        self.context['payment'] = payment.pk
        payment.date = datetime.today().date()
        payment.total_price = self.context['total_price']
        payment.currency = self.request.session['currency_selected']
        SQL.Save(data=payment)

    def Load_Payment_Details(self):

        model_manager = Payment_Models_Manager(self)
        payment = model_manager.Get_Cart()
        payment.Update_Total_Price(self)

        self.context['user'] = self.request.session['user_user']
        self.context['cart'] = SQL.Filter(Model_Payment_Product, payment=payment)
        self.context['total_price'] = payment.total_price
        self.context['delivery'] = payment.delivery_price
        self.context['address'] = SQL.Filter(Model_User_Address, user=self.context['user'])
        self.Update_Payment()

    def Create_Address(self, pk, model):

        user_address = SQL.Get(Model_User_Address, pk=pk)
        address = None

        user = self.request.session['user_user']
        payment = SQL.Get(Model_Payment, user=user, status='cart')

        if model == 'delivery_address':
            address = SQL.Get(Model_Delivery_Address, payment=payment)

        if model == 'invoice_address':
            address = SQL.Get(Model_Invoice_Address, payment=payment)

        address.full_name = user_address.full_name
        address.address_line = user_address.address_line
        address.city = user_address.city
        address.region = user_address.region
        address.postcode = user_address.postcode
        address.country = user_address.country
        SQL.Save(data=address)

    def Manage_Content(self):
        self.Load_Payment_Details()
        return self.Render_HTML('payment/payment.html')


    def Manage_Form_Address_Payment(self):

        address_payment_pk = self.request.POST['shipment']
        address_invoice_pk = self.request.POST['invoice']

        self.Create_Address(address_payment_pk, 'delivery_address')
        self.Create_Address(address_invoice_pk, 'invoice_address')

        self.Load_Payment_Details()
        self.context['paypal'] = PayPal(self.request).Create_From(self)
        self.context['dotpay'] = DotPay(self.request).Create_From(self)

        self.context['address_is_validate'] = True
        return self.Render_HTML('payment/payment.html')

    def Manage_Form(self):

        # the second step in payment
        if self.request.POST['_name_'] == 'address':
            return self.Manage_Form_Address_Payment()

        return Website_Manager.Manage_Form(self)


    def Manage_Get_Delivery(self):

        address = SQL.Get(Model_User_Address, pk=self.request.POST['value'])
        delivery = SQL.Get(Model_Delivery, country=address.country)
        user = self.request.session['user_user']
        payment = SQL.Get(Model_Payment, user=user, status='cart')

        payment.delivery_price = delivery
        SQL.Save(data=payment)

        prices = {
            'eur': delivery.price_eur,
            'pln': delivery.price_pln,
        }

        return JsonResponse(prices)

    def Manage_Get(self):

        if self.request.POST['__get__'] == 'delivery':
            return self.Manage_Get_Delivery()

        return Website_Manager.Manage_Get(self)

    @staticmethod
    def Launch(request):
        return Payment_Manager(request, authorization=True).HTML



class Apply_Payment(Website_Manager):

    def Manage_Content(self):
        return self.Render_HTML('payment/apply.html')

    def Error_No_Event(self):
        return self.Index()

    @staticmethod
    @csrf_exempt
    def Launch(request):
        return Apply_Payment(request).HTML



class Cancel_Payment(Website_Manager):

    def Manage_Content(self):
        return self.Render_HTML('payment/cancel.html')

    def Error_No_Event(self):
        return self.Index()

    @staticmethod
    @csrf_exempt
    def Launch(request):
        return Cancel_Payment(request).HTML

