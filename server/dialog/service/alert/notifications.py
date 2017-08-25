from server.dialog.service.base import *
from server.service.notification.models import *


class Service_Notifications(Base_Service):

    def Manage(self):
        self.context['notifications'] = SQL.All(
            Notification_Model).order_by('-date')[:10]

        return self.Render_Dialog('notifications.html')
