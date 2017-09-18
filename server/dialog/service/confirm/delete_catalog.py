from server.dialog.service.base import *


class Service_Delete_Catalog(Base_Service):

    def Manage(self):
        self.context['title'] = Text(self, 203)
        self.context['text'] = Text(self, 204)
        return self.Render_Dialog('confirm.html', only_root=True)
