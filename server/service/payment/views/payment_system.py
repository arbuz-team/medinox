from server.service.sender.views import *


class Payment_System(Base_Website):

    def Send_Confirm(self):

        email = self.payment.user.email
        content = {
            'payment': self.payment,
            'selected_products': Selected_Product.
                objects.filter(payment=self.payment)
        }

        if self.valid:

            generator = Generator_PDF(self.request, authorization=True)
            pdf = generator.Invoice(self.payment.pk)
            Sender(self.request).Send_Payment_Approved(content, email, pdf)

        else: Sender(self.request).Send_Payment_Failure(content, email)

    def __init__(self, request):
        Base_Website.__init__(self, request)
        Check_Session(request)

        self.payment = None
        self.valid = False
