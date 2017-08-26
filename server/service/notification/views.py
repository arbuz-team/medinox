from server.manage.switch.website import *
from server.service.notification.models import *


class Notification_Manager(Website_Manager):

    def Manage_Get_Next_Ten_Notifications(self):
        last_notification_pk = self.request.POST['last_notification_pk']

        # when not defined, then first records
        if not last_notification_pk:

            self.context['notifications'] = SQL.Filter(
                Notification_Model).order_by('-pk')[:10]

        else:

            # records after date from last_notification_pk
            last = SQL.Get(Notification_Model, pk=last_notification_pk)
            self.context['notifications'] = SQL.Filter(Notification_Model,
                pk__lt=last.pk).order_by('-pk')[:10]

        return self.Render_HTML('notification/list.html')

    def Manage_Get(self):

        if self.request.POST['_name_'] == 'ten_notifications':
            return self.Manage_Get_Next_Ten_Notifications()

    @staticmethod
    def Launch(request):
        return Notification_Manager(request).HTML
