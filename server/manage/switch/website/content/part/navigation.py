from server.manage.switch.website.endpoints import *


class Navigation(Endpoints):

    def Manage_Content(self):
        return self.Render_HTML('navigation/navigation.html')
