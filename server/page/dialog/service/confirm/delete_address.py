from server.page.dialog.service.base import *


class Service_Delete_Address(Base_Service):

    def Manage(self):
        self.content['title'] = Text(self.request, 107)
        self.content['text'] = Text(self.request, 108)
        return self.Render_Dialog('confirm.html', authorization=True)
