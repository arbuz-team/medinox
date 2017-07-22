from server.service.sender.views import *


class Payment_System(Base_Website):

    def Send_Confirm(self):

        email = self.payment.user.email
        content = {
            'payment': self.payment,
            'selected_products': SQL.Filter(
                Selected_Product, payment=self.payment)
        }

        if self.valid:

            generator = Generator_PDF(self.request, authorization=True)
            pdf = generator.Invoice(self.payment.pk)
            Sender(self).Send_Payment_Approved(content, email, pdf)

        else: Sender(self).Send_Payment_Failure(content, email)

    def __init__(self, request):
        self.request = request

        Base_Website.__init__(self, self)
        Check_Session(request)

        self.payment = None
        self.valid = False
