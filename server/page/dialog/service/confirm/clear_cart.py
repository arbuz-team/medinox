from server.page.dialog.service.base import *


class Service_Clear_Cart(Base_Service):

    def Manage(self):
        self.content['title'] = Text(self.request, 100)
        self.content['text'] = Text(self.request, 101)
        return self.dialog.Render_Dialog(
            'dialog/confirm.html', authorization=True)
