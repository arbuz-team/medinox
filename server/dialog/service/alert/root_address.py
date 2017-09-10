from server.dialog.service.base import *
from server.service.payment.models import *


class Service_Root_Address(Base_Service):

    def Manage(self):

        pk = self.request.POST['value']
        payment = SQL.Get(Model_Payment, pk=pk)

        self.context['invoice'] = SQL.Get(Model_Invoice_Address, payment=payment)
        self.context['delivery'] = SQL.Get(Model_Delivery_Address, payment=payment)

        return self.Render_Dialog('address.html', only_root=True)
