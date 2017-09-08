from server.dialog.service.base import *


class Service_Delete_Home(Base_Service):

    def Manage(self):
        self.context['title'] = Text(self, 187)
        self.context['text'] = Text(self, 188)
        return self.Render_Dialog('confirm.html', only_root=True)
