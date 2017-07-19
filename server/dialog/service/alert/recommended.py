from server.dialog.service.base import *


class Service_Recommended(Base_Service):

    def Manage(self):
        self.context['title'] = Text(self, 9)
        self.context['text'] = Text(self, 10)
        return self.Render_Dialog('alert.html', only_root=True)
