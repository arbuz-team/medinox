from server.manage.user.forms import *


class User_Agreement(Website_Manager):

    def Manage_Content(self):
        self.context['form_markdown'] = Form_Markdown()
        return self.Render_HTML('user/agreement.html')

    @staticmethod
    def Launch(request):
        return User_Agreement(request).HTML
