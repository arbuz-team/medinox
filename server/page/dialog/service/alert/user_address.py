from server.page.dialog.service.base import *


class Service_User_Address(Base_Service):

    def Manage(self):

        pk = self.request.POST['dialog_value']
        payment = SQL.Get(Payment, pk=pk)

        self.content['invoice'] = SQL.Get(Invoice_Address, payment=payment)
        self.content['delivery'] = SQL.Get(Delivery_Address, payment=payment)

        return self.Render_Dialog('address.html', authorization=True)
