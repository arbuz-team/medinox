from server.page.dialog.service.base import *


class Service_Recommended(Base_Service):

    def Manage(self):
        self.content['title'] = Text(self.request, 9)
        self.content['text'] = Text(self.request, 10)
        return self.Render_Dialog('alert.html', only_root=True)