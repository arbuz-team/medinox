from server.page.dialog.service.base import *


class Service_Icons(Base_Service):

    def Manage(self):
        self.content['title'] = Text(self, 137)
        self.content['text'] = Text(self, 138)
        return self.Render_Dialog('alert.html')
