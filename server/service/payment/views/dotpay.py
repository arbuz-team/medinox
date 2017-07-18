from server.service.payment.forms import *
from .payment_system import *

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