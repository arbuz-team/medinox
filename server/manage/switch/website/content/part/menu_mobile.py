from server.manage.switch.website.endpoints import *


class Menu_Mobile(Endpoints):

    def Manage_Content(self):
        return self.Render_HTML('part/menu_mobile.html')
