from server.dialog.service.base import *


class Service_Delete_About(Base_Service):

    def Manage(self):
        self.content['title'] = Text(self, 153)
        self.content['text'] = Text(self, 154)
        return self.Render_Dialog('confirm.html', only_root=True)