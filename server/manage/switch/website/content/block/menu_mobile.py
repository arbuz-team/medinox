from server.manage.switch.website.endpoints import *


class Menu_Mobile_Part(Endpoints):

    def Manage_Content(self):
        return self.Render_HTML('block/menu_mobile.html')
