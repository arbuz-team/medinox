from server.service.payment.views.payment_method.dotpay import *
from server.service.payment.views.payment_method.paypal import *
from server.manage.switch.website.content.block.cart import *
from server.manage.switch.website.manager import *


class Payment_Manager(Website_Manager):

    # redirect

    def Manage_Little_Form(self):
        return Cart_Block(self).Manage_Little_Form()

    def Manage_Button(self):
        return Cart_Block(self).Manage_Button()

    # content

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

    def Manage_Content(self):
        self.Load_Payment_Details()
        return self.Render_HTML('payment/payment.html')

    # forms

    def Calculate_Delivery_Price(self):

        model_manager = Payment_Models_Manager(self)
        payment = model_manager.Get_Cart()

        products_with_force_price = SQL.Filter(Model_Payment_Product,
                payment=payment, product__force_delivery_price__gt=0)

        # standard delivery price - from root panel
        delivery = SQL.First(Model_Delivery)
        currency_manager = Base_Currency_Manager(self)
        self.context['delivery_price'] = currency_manager.Get_Price(delivery.delivery_price)
        self.context['cash_on_delivery'] = currency_manager.Get_Price(delivery.cash_on_delivery)

        # one product have force price - big package
        if len(products_with_force_price) == 1:

            price = products_with_force_price[0]\
                .product.force_delivery_price

            self.context['delivery_price'] += currency_manager.Get_Price(price)
            self.context['cash_on_delivery'] += currency_manager.Get_Price(price)

        # more than one product with force price - ask seller
        elif len(products_with_force_price) > 1:

            self.context['delivery_price'] = Text(self, 262)
            self.context['cash_on_delivery'] = Text(self, 262)

    def Create_Address(self, pk, model):

        user_address = SQL.Get(Model_User_Address, pk=pk)
        address = None

        user = self.request.session['user_user']
        payment = SQL.Get(Model_Payment, user=user, status='cart')

        if model == 'delivery_address':
            address = SQL.Get(Model_Delivery_Address, payment=payment)

        if model == 'invoice_address':
            address = SQL.Get(Model_Invoice_Address, payment=payment)

        address.name = user_address.name
        address.surname = user_address.surname
        address.company_name = user_address.company_name
        address.nip = user_address.nip
        address.address_line = user_address.address_line
        address.city = user_address.city
        address.region = user_address.region
        address.postcode = user_address.postcode
        address.country = user_address.country
        SQL.Save(data=address)

    def Manage_Form_Address_Payment(self):

        address_payment_pk = self.request.POST['shipment']
        address_invoice_pk = self.request.POST['invoice']

        self.Create_Address(address_payment_pk, 'delivery_address')
        self.Create_Address(address_invoice_pk, 'invoice_address')
        self.Calculate_Delivery_Price()

        return self.Render_HTML('payment/payment_delivery.html')

    def Manage_Form_Delivery(self):

        # avaible methods
        delivery_methods = {
            'courier': 263,
            'cash_on_delivery': 264,
            'personal_receipt': 265,
        }

        # get payment
        model_manager = Payment_Models_Manager(self)
        payment = model_manager.Get_Cart()

        # save delivery method
        method = self.request.POST['delivery']
        payment.delivery_method = delivery_methods[method]

        # save delivery price
        self.Calculate_Delivery_Price()
        delivery = self.request.POST['delivery']

        try:

            payment.delivery_price = {
                'courier': float(self.context['delivery_price']),
                'cash_on_delivery': float(self.context['cash_on_delivery']),
                'personal_receipt': 0,
            }[delivery]

        except: payment.delivery_price = 0

        # client don't pay
        if delivery == 'personal_receipt':

            payment.delivery_method = Text(self, 267)
            payment.status = 'pending'
            SQL.Save(data=payment)

            path_manager = Path_Manager(self)
            url = path_manager.Get_Path(
                'payment.apply', current_language=True)

            return HttpResponseRedirect(url)

        # for third step - pay
        self.Load_Payment_Details()
        self.context['paypal'] = PayPal(self.request).Create_From(self)
        self.context['dotpay'] = DotPay(self.request).Create_From(self)
        SQL.Save(data=payment)

        methods = SQL.All(Model_Payment_Method)
        self.context['avaible'] = {m.method:m.is_active for m in methods}
        return self.Render_HTML('payment/payment_service.html')

    def Manage_Form(self):

        # the second step in payment
        if self.request.POST['_name_'] == 'address':
            return self.Manage_Form_Address_Payment()

        # the third step in payment
        if self.request.POST['_name_'] == 'delivery':
            return self.Manage_Form_Delivery()

        return Website_Manager.Manage_Form(self)

    # get

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

