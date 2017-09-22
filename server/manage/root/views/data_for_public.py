from server.manage.switch.website.manager import *
from server.service.payment.forms import *


class Data_For_Public(Website_Manager):

    def Manage_Content(self):
        self.context['values'] = SQL.First(Model_Data_For_Public)
        return self.Render_HTML('root/data_for_public.html')

    def Manage_Form(self):
            return HttpResponse()

    @staticmethod
    def Launch(request):
        return Data_For_Public(request, only_root=True).HTML
