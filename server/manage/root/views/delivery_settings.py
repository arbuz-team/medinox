from server.manage.switch.website.manager import *
from server.service.payment.forms import *


class Delivery_Settings(Website_Manager):

    def Manage_Content(self):
        self.context['delivery'] = SQL.First(Model_Delivery)
        return self.Render_HTML('root/delivery_settings.html')

    def Manage_Form(self):

        if self.request.POST['_name_'] == 'delivery_settings':
            delivery = SQL.First(Model_Delivery)

            if self.request.POST['delivery_price']:
                delivery.delivery_price = \
                    self.request.POST['delivery_price']

            if self.request.POST['cash_on_delivery']:
                delivery.cash_on_delivery = \
                    self.request.POST['cash_on_delivery']

            SQL.Save(data=delivery)
            return HttpResponse()

    @staticmethod
    def Launch(request):
        return Delivery_Settings(request, only_root=True).HTML
