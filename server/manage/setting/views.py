from server.manage.switch.views import *
from server.manage.user.models import *
from server.manage.root.models import *
import os

from server.manage.setting.script import cosmetix


class Control_Panel(Dynamic_Event_Manager):

    def Manage_Content_Ground(self):
        return self.Render_HTML('setting/control_panel.html')

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

        if self.request.POST['__button__'] == 'reset_passwords':
            return self.Manage_Button_Reset_Passwords()

        return Dynamic_Event_Manager.Manage_Button(self)

    @staticmethod
    def Launch(request):
        return Control_Panel(request, only_root=True).HTML

