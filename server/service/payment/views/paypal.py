from server.service.payment.forms import *
from .payment_system import *


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
            'amount':           self.context['total_price'],
            'custom':           self.context['payment'],
            'currency_code':    self.request.session['currency_selected'],

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
