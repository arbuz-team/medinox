from server.page.dialog.service.base import *


class Service_Product_Recommended(Base_Service):

    def Manage(self):
        self.content['title'] = Text(self.request, 9)
        self.content['text'] = Text(self.request, 10)
        return self.dialog.Render_Dialog(
            'dialog/alert.html', only_root=True)
