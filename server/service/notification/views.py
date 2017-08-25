from server.manage.switch.website import *
from server.service.notification.models import *


class Notification_Manager(Website_Manager):

    def Manage_Get_Next_Ten_Notifications(self):

        last_notification_id = self.request.POST['last_notification_id']
        date = SQL.Get(Notification_Model, id=last_notification_id).date

        self.context['notifications'] = SQL.Filter(
            Notification_Model, date__lt=date)[:10]

        return self.Render_HTML('notification/list.html')

    def Manage_Get(self):

        if self.request.POST['__get__'] == 'ten_notifications':
            return self.Manage_Get_Next_Ten_Notifications()

    @staticmethod
    def Launch(request):
        return Notification_Manager(request).HTML
