from server.dialog.service.base import *


class Service_Delete_Address(Base_Service):

    def Manage(self):
        self.context['title'] = Text(self, 107)
        self.context['text'] = Text(self, 108)
        return self.Render_Dialog('confirm.html', authorization=True)
