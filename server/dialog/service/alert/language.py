from server.dialog.service.base import *


class Service_Language(Base_Service):

    def Manage(self):
        return self.Render_Dialog('language.html')
