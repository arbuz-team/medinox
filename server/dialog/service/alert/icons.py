from server.dialog.service.base import *


class Service_Icons(Base_Service):

    def Manage(self):
        self.context['title'] = Text(self, 137)
        self.context['text'] = Text(self, 138)
        return self.Render_Dialog('alert.html')
