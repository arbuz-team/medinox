from server.manage.user.forms import *


class Approved_Register(Website_Manager):

    def Manage_Content(self):
        return self.Render_HTML('user/approved.html')

    @staticmethod
    def Update_User_Status(request, key):
        all_keys = No_Approved_User.objects.values('approved_key')

        if {'approved_key': key} in all_keys:
            record = SQL.Get(No_Approved_User, approved_key=key)
            record.user.approved = True
            SQL.Save(data=record.user)

            SQL.Delete(data=record)

        return Approved_Register(request, length_navigation=2).HTML

    @staticmethod
    def Launch(request):
        return Approved_Register(request).HTML
