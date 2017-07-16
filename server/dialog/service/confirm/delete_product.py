from server.dialog.service.base import *


class Service_Delete_Product(Base_Service):

    def Manage(self):
        self.content['title'] = Text(self, 98)
        self.content['text'] = Text(self, 99)
        return self.Render_Dialog('confirm.html', only_root=True)
