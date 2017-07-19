from server.dialog.service.base import *


class Service_Delete_Product(Base_Service):

    def Manage(self):
        self.context['title'] = Text(self, 98)
        self.context['text'] = Text(self, 99)
        return self.Render_Dialog('confirm.html', only_root=True)
