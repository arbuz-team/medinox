from server.manage.switch.website.endpoints import *


class Header(Endpoints):

    def Manage_Content(self):
        return self.Render_HTML('header/header.html')
