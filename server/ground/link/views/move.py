from server.manage.switch.website import *


class Move_Link(Website_Manager):

    def Manage_Form(self):
        return HttpResponse()

    @staticmethod
    def Launch(request):
        return Move_Link(request, only_root=True).HTML
