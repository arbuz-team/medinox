from server.page.dialog.service.base import *


class Service_Delete_About(Base_Service):

    def Manage(self):
        self.content['title'] = Text(self.request, 153)
        self.content['text'] = Text(self.request, 154)
        return self.dialog.Render_Dialog(
            'dialog/confirm.html', only_root=True)