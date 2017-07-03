from server.page.dialog.service.base import *


class Service_Delete_Description(Base_Service):

    def Manage(self):
        self.content['title'] = Text(self.request, 160)
        self.content['text'] = Text(self.request, 161)
        return self.Render_Dialog('confirm.html', only_root=True)
