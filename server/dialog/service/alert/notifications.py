from server.dialog.service.base import *


class Service_Notifications(Base_Service):

    def Manage(self):
        return self.Render_Dialog('notifications.html')
