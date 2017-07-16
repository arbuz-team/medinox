from server.dialog.service.base import *


class Service_Delete_Address(Base_Service):

    def Manage(self):
        self.content['title'] = Text(self, 107)
        self.content['text'] = Text(self, 108)
        return self.Render_Dialog('confirm.html', authorization=True)
