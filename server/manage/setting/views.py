from server.manage.switch.website.manager import *
from server.manage.user.models import *
from server.manage.root.models import *
import os


class Control_Panel(Website_Manager):

    def Manage_Content(self):
        return self.Render_HTML('setting/control_panel.html')

    @staticmethod
    def Manage_Button_Reset_Passwords():

        user = SQL.Get(Model_User, username='Drego31')
        user.password = Base_Website.Encrypt('kaktus88')
        SQL.Save(data=user)

        root = SQL.First(Model_Root)
        root.password = Base_Website.Encrypt('kaktus88')
        SQL.Save(data=root)

        return HttpResponse()

    def Manage_Button(self):

        if self.request.POST['_name_'] == 'reset_passwords':
            return self.Manage_Button_Reset_Passwords()

    @staticmethod
    def Launch(request):
        return Control_Panel(request, only_root=True).HTML

