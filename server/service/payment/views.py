from server.service.payment.forms import *
from server.service.sender.views import *


class Payment_System(Dynamic_Base):

    def Send_Confirm(self):

        email = self.payment.user.email
        content = {
            'payment': self.payment,
            'selected_products': Selected_Product.
                objects.filter(payment=self.payment)
        }

        if self.valid:

            generator = Generator_PDF(self.request, authorization=True)
            pdf = generator.Invoice(self.payment.pk)
            Sender(self.request).Send_Payment_Approved(content, email, pdf)

        else: Sender(self.request).Send_Payment_Failure(content, email)

    def __init__(self, request):
        Dynamic_Base.__init__(self, request)
        Check_Session(request)

        self.payment = None
        self.valid = False



class PayPal(Payment_System):

    def Valid_PayPal(self):
        post = self.request.POST

        if post['payment_status'] == 'Completed':
            self.payment = SQL.Get(Payment, pk=post['custom'])

            # check receiver
            if post['receiver_email'] != PAYPAL_RECEIVER_EMAIL:
                return

            # check amount paid
            if str(post['mc_gross']) != self.payment.total_price:
                return

            # check currency
            if post['mc_currency'] != self.payment.currency:
                return

            self.payment.status = 'pending'
            self.payment.service = 'PayPal'
            SQL.Save(data=self.payment)

            self.valid = True

    def Create_PayPal_From(self):
        path_manager = Path_Manager(self)

        paypal_dict = \
        {
            'business':         PAYPAL_RECEIVER_EMAIL,
            'item_name':        'medifiller',
            'amount':           self.content['total_price'],
            'custom':           self.content['payment'],
            'currency_code':    self.request.session['translator_currency'],

            'notify_url':       path_manager.Get_Urls('payment.paypal', current_language=True),
            'return':           path_manager.Get_Urls('payment.apply', current_language=True),
            'cancel_return':    path_manager.Get_Urls('payment.cancel', current_language=True),
        }

        return Form_PayPal(self, initial=paypal_dict)

    @staticmethod
    @csrf_exempt
    @require_POST
    def Service(request):
        paypal = PayPal(request)
        paypal.Display_Status()
        paypal.Valid_PayPal()
        paypal.Send_Confirm()
        return HttpResponse('OKAY')



class DotPay(Payment_System):

    def Valid_DotPay(self):
        post = self.request.POST

        if post['operation_status'] == 'completed':
            self.payment = SQL.Get(Payment, pk=post['control'])

            # check receiver
            if post['id'] != DOTPAY_RECEIVER_ID:
                return

            # check amount paid
            if post['operation_currency'] != self.payment.currency:
                return

            # check currency
            if post['operation_amount'] != self.payment.total_price:
                return

            self.payment.status = 'pending'
            self.payment.service = 'DotPay'
            SQL.Save(data=self.payment)

            self.valid = True

    def Create_DotPay_From(self):
        payment = SQL.Get(Payment, pk=self.content['payment'])
        address = SQL.Filter(User_Address, user=payment.user)[0]
        path_manager = Path_Manager(self)

        dotpay_dict = \
        {
            'id':           DOTPAY_RECEIVER_ID,
            'amount':       self.content['total_price'],
            'currency':     self.request.session['translator_currency'],
            'description':  Text(self, 152),

            'control':      self.content['payment'],
            'firstname':    address.full_name.split(' ')[0],
            'lastname':     address.full_name.split(' ')[1],
            'email':        payment.user.email,

            'lang':         self.request.session['translator_language'].lower(),

            'URL':          path_manager.Get_Urls('payment.apply', current_language=True),
            'URLC':         path_manager.Get_Urls('payment.dotpay', current_language=True),
        }

        return Form_Dotpay(self, initial=dotpay_dict)

    @staticmethod
    @csrf_exempt
    @require_POST
    def Service(request):
        dotpay = DotPay(request)
        dotpay.Display_Status()
        dotpay.Valid_DotPay()
        dotpay.Send_Confirm()
        return HttpResponse('OK')



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

        model_manager = Payment_Models_Manager(self.request)
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
