from server.manage.switch.website.manager import *
from server.service.payment.forms import *


class Delivery_Settings(Website_Manager):

    def Manage_Content(self):
        self.context['delivery'] = SQL.First(Model_Delivery)
        return self.Render_HTML('root/delivery_settings.html')

    def Manage_Form(self):

        if self.request.POST['_name_'] == 'delivery_settings':
            delivery = SQL.First(Model_Delivery)

            if self.request.POST['price_on_receipt']:
                delivery.price_on_receipt = \
                    self.request.POST['price_on_receipt']

            if self.request.POST['price_in_advance']:
                delivery.price_on_receipt = \
                    self.request.POST['price_in_advance']

            SQL.Save(data=delivery)
            return HttpResponse()

    @staticmethod
    def Launch(request):
        return Delivery_Settings(request, only_root=True).HTML
