from server.dialog.service.base import *


class Service_Delete_Description(Base_Service):

    def Manage(self):
        self.content['title'] = Text(self, 160)
        self.content['text'] = Text(self, 161)
        return self.Render_Dialog('confirm.html', only_root=True)
