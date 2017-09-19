from server.ground.product.views import *
from server.manage.switch.paths import *


class Panel_App(Website_Manager):

    def Manage_Content(self):
        path_manager = Path_Manager(self)
        return HttpResponseRedirect(path_manager.Get_Path(
            'catalog.switcher.empty', current_language=True))

    @staticmethod
    def Launch(request):
        return Panel_App(request).HTML
