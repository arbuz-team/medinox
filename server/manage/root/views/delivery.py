from server.manage.switch.website.manager import *
from server.service.payment.forms import *


class Delivery_Settings(Website_Manager):

    def Manage_Content(self):
        self.context['options'] = SQL.All(Model_Delivery)
        return self.Render_HTML('root/delivery_settings.html')

    def Manage_Form(self):

        pk, currency = self.request.POST['_name_'].split(' ')
        price = float(self.request.POST['value']) * 100
        delivery = SQL.Get(Model_Delivery, pk=pk)

        if currency == 'PLN':
            delivery.price_pln = price

        if currency == 'EUR':
            delivery.price_eur = price

        SQL.Save(data=delivery)
        return HttpResponse()

    @staticmethod
    def Launch(request):
        return Delivery_Settings(request, only_root=True).HTML
