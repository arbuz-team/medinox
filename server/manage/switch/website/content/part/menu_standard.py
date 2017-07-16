from server.manage.switch.website.endpoints import *


class Menu_Standard(Endpoints):

    def Manage_Content(self):
        return self.Render_HTML('part/menu_standard.html')
