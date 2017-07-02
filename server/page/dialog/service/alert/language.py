from server.page.dialog.service.base import *


class Service_Language(Base_Service):

    def Manage(self):
        return self.dialog.Render_Dialog(
            'dialog/language.html')
