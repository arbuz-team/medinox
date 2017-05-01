from arbuz.views import *
from user.models import *
from root.models import *
import os

from setting.script import cosmetix


class Control_Panel(Dynamic_Event_Manager):

    def Manage_Content_Ground(self):
        return self.Render_HTML('setting/control_panel.html')

    @staticmethod
    def Manage_Button_Reset_Database():
        os.system(BASE_DIR + '/reset.sh')
        return JsonResponse({'__button__': 'true'})

    def Manage_Button_Load_Product(self):
        self.Manage_Button_Reset_Database()
        cosmetix.Start()
        return JsonResponse({'__button__': 'true'})

    @staticmethod
    def Manage_Button_Reset_Passwords():
        user = User.objects.get(username='Drego31')
        user.password = Dynamic_Base.Encrypt('kaktus88')
        user.save()
        root = Root.objects.first()
        root.password = Dynamic_Base.Encrypt('kaktus88')
        root.save()
        return JsonResponse({'__button__': 'true'})

    def Manage_Button(self):

        if self.request.POST['__button__'] == 'reset_databases':
            return self.Manage_Button_Reset_Database()

        if self.request.POST['__button__'] == 'load_product':
            return self.Manage_Button_Load_Product()

        if self.request.POST['__button__'] == 'reset_passwords':
            return self.Manage_Button_Reset_Passwords()

        return Dynamic_Event_Manager.Manage_Button(self)

    @staticmethod
    def Launch(request):
        return Control_Panel(request).HTML

