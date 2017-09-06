from server.manage.switch.website import *


class Copy_Link(Website_Manager):

    def Manage_Form(self):
        return HttpResponse()

    @staticmethod
    def Launch(request):
        return Copy_Link(request, only_root=True).HTML
