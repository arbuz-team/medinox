from server.manage.switch.website.manager import *
from server.service.payment.forms import *


class Data_For_Public(Website_Manager):

    def Manage_Content(self):
        self.context['values'] = SQL.First(Model_Data_For_Public)
        return self.Render_HTML('root/data_for_public.html')

    def Manage_Form(self):

        self.Clear_Session('root_for_public')
        data = SQL.First(Model_Data_For_Public)
        data.names = False
        data.phones = False
        data.address = False
        data.email = False

        if 'names' in self.request.POST:
            data.names = True

        if 'phones' in self.request.POST:
            data.phones = True

        if 'address' in self.request.POST:
            data.address = True

        if 'email' in self.request.POST:
            data.email = True

        SQL.Save(data=data)
        return HttpResponse()

    @staticmethod
    def Launch(request):
        return Data_For_Public(request, only_root=True).HTML
