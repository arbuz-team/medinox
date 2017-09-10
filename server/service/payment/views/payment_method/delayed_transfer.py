from server.service.payment.models import *
from server.manage.switch.website import *


class Delayed_Transfer(Website_Manager):

    def Manage_Content(self):

        user = self.request.session['user_user']
        payment = SQL.Get(Model_Payment,
            user=user, status='cart')

        payment.status = 'pending'
        payment.service = 'Delayed transfer'
        SQL.Save(data=payment)

        return HttpResponseRedirect('/payment/apply/')

    @staticmethod
    def Service(request):
        return Delayed_Transfer(request).HTML
