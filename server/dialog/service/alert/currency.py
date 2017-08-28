from server.dialog.service.base import *


class Service_Currency(Base_Service):

    def Manage(self):
        return self.Render_Dialog('currency.html')
