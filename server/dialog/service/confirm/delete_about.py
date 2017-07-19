from server.dialog.service.base import *


class Service_Delete_About(Base_Service):

    def Manage(self):
        self.context['title'] = Text(self, 153)
        self.context['text'] = Text(self, 154)
        return self.Render_Dialog('confirm.html', only_root=True)
