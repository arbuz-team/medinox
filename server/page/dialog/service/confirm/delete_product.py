from server.page.dialog.service.base import *


class Service_Delete_Product(Base_Service):

    def Manage(self):
        self.content['title'] = Text(self.request, 98)
        self.content['text'] = Text(self.request, 99)
        return self.dialog.Render_Dialog(
            'dialog/confirm.html', only_root=True)
