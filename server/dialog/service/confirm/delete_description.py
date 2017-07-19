from server.dialog.service.base import *


class Service_Delete_Description(Base_Service):

    def Manage(self):
        self.context['title'] = Text(self, 160)
        self.context['text'] = Text(self, 161)
        return self.Render_Dialog('confirm.html', only_root=True)
