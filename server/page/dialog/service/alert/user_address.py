from server.page.dialog.service.base import *


class Service_User_Address(Base_Service):

    def Manage(self):

        pk = self.request.POST['dialog_value']
        payment = Payment.objects.get(pk=pk)

        self.content['invoice'] = Invoice_Address.objects.get(payment=payment)
        self.content['delivery'] = Delivery_Address.objects.get(payment=payment)

        return self.dialog.Render_Dialog(
            'dialog/address.html', authorization=True)
