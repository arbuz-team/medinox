from server.manage.user.forms import *


class Sign_Out(Website_Manager):

    def Manage_Content(self):
        self.Clear_Session('user_')
        return self.Render_HTML('user/sign_out.html')

    @staticmethod
    def Launch(request):
        return Sign_Out(request, authorization=True).HTML
