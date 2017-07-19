from server.dialog.service.base import *


class Service_Clear_Cart(Base_Service):

    def Manage(self):
        self.context['title'] = Text(self, 100)
        self.context['text'] = Text(self, 101)
        return self.Render_Dialog('confirm.html', authorization=True)
