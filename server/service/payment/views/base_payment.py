from server.service.sender.views import *


class Base_Payment(Base_Website):

    @abstractmethod
    def Valid(self):
        pass

    @abstractmethod
    def Create_From(self, *args, **kwargs):
        pass

    def Display_Status(self):
        status_manager = Status_Manager(self)
        status_manager.Timer_Start()
        status_manager.Display_Status()

    def Send_Confirm(self):

        email = self.payment.user.email
        content = {
            'payment': self.payment,
            'selected_products': SQL.Filter(
                Model_Payment_Product, payment=self.payment)
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
