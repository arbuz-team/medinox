from server.manage.switch.website.manager import *
from server.service.payment.forms import *


class Payment_Settings(Website_Manager):

    def Manage_Content(self):
        self.context['payment_method'] = SQL.All(Model_Payment_Method)
        return self.Render_HTML('root/payment_settings.html')

    def Manage_Form(self):

        if self.request.POST['_name_'] == 'payment_settings':

            keys = self.request.POST.keys()

            methods = SQL.All(Model_Payment_Method)
            for method in methods:
                method.is_active = False
                SQL.Save(data=method)

            for key in keys:

                if not SQL.Filter(Model_Payment_Method, method=key):
                    continue

                method = SQL.Get(Model_Payment_Method, method=key)
                method.is_active = True
                SQL.Save(data=method)

            return HttpResponse()

    @staticmethod
    def Launch(request):
        return Payment_Settings(request, only_root=True).HTML
