from server.dialog.service.base import *
from server.service.payment.forms.address import *


class Service_Address_Payment(Base_Service):

    def Edit(self):

        _type = self.dialog.Get_Post_Other('type')
        pk = self.request.POST['value']
        instance = None

        if _type == 'delivery':

            instance = SQL.Get(Model_Delivery_Address, pk=pk)
            self.context['form'] = Form_Delivery_Address(
                self, instance=instance)

        if _type == 'invoice':

            instance = SQL.Get(Model_Invoice_Address, pk=pk)
            self.context['form'] = Form_Invoice_Address(
                self, instance=instance)

        self.context['payment'] = instance.payment
        self.request.session['root_edit_payment_address'] = \
            instance

    def Not_Valid(self):
        self.context['title'] = Text(self, 268)
        return self.Render_Dialog(
            'address_for_payment.html',
            'payment_address', only_root=True)

    def Manage(self):

        # always edit
        self.Edit()
        self.context['title'] = Text(self, 268)
        return self.Render_Dialog(
            'address_for_payment.html',
            'payment_address', only_root=True)
