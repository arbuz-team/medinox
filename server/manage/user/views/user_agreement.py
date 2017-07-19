from server.manage.user.forms import *


class User_Agreement(Website_Manager):

    def Manage_Content(self):
        return self.Render_HTML('user/agreement.html')

    @staticmethod
    def Launch(request):
        return User_Agreement(request).HTML
