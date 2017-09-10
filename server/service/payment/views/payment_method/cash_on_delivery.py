from server.service.payment.models import *
from server.manage.switch.website import *


class Cash_On_Delivery(Website_Manager):

    def Manage_Content(self):

        user = self.request.session['user_user']
        payment = SQL.Get(Model_Payment,
            user=user, status='cart')

        payment.status = 'pending'
        payment.service = 'Cash on delivery'
        SQL.Save(data=payment)

        return HttpResponseRedirect('/payment/apply/')

    @staticmethod
    def Service(request):
        return Cash_On_Delivery(request).HTML
