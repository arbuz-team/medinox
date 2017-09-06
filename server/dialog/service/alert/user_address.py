from server.dialog.service.base import *


class Service_User_Address(Base_Service):

    def Manage(self):

        pk = self.request.POST['value']
        payment = SQL.Get(Model_Payment, pk=pk)

        self.context['invoice'] = SQL.Get(Model_Invoice_Address, payment=payment)
        self.context['delivery'] = SQL.Get(Model_Delivery_Address, payment=payment)

        return self.Render_Dialog('address.html', authorization=True)
