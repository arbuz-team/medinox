from server.page.dialog.service.base import *


class Service_Clear_Cart(Base_Service):

    def Manage(self):
        self.content['title'] = Text(self, 100)
        self.content['text'] = Text(self, 101)
        return self.Render_Dialog('confirm.html', authorization=True)
