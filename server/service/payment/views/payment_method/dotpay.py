from server.service.payment.forms import *
from server.service.payment.views.base_payment import *

class DotPay(Base_Payment):

    def Valid(self):
        post = self.request.POST

        if post['operation_status'] == 'completed':
            self.payment = SQL.Get(Model_Payment, pk=post['control'])

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

    def Create_From(self, _object):
        payment = SQL.Get(Model_Payment, pk=_object.context['payment'].pk)
        address = SQL.Filter(Model_User_Address, user=payment.user)[0]
        path_manager = Path_Manager(self)

        dotpay_dict = \
        {
            'id':           DOTPAY_RECEIVER_ID,
            'amount':       _object.context['total_price'],
            'currency':     self.request.session['currency_selected'],
            'description':  Text(self, 152),

            'control':      _object.context['payment'].pk,
            'firstname':    address.name,
            'lastname':     address.surname,
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
        dotpay.Valid()
        dotpay.Send_Confirm()
        return HttpResponse('OK')
