from server.manage.switch.website.base import *
from server.service.payment.models import *
from server.service.notification.models import *


class Refresh(Base_Website):

    def Update_Navigation(self):

        navigation = []
        url = self.request.get_full_path()
        parts_of_url = url.split('/')[1:-1]
        page = '/'

        for part in parts_of_url:
            page += part + '/'
            navigation.append((part, page))

        if self.length_navigation:
            navigation = navigation[0:self.length_navigation]

        self.request.session['arbuz_navigation'] = navigation

    def Update_Current_Url(self):
        path_manager = Path_Manager(self)
        self.request.session['arbuz_url'] = \
            path_manager.Get_Urls()

    def Update_Website_Permissions(self):
        # the method update permissions for HTML

        self.request.session['arbuz_permissions'] = ''
        if '__content__' not in self.request.POST:
            return

        if self.request.POST['__content__'] == 'ground':

            if self.only_root:
                self.request.session['arbuz_permissions'] = 'only_root'

            if self.authorization:
                self.request.session['arbuz_permissions'] = 'authorization'

    def Update_Redirect_URL(self):
        self.context['go_back'] = '/'

        if 'redirect' in self.other_value:
            self.context['go_back'] = base64.b64decode(
                bytes(self.other_value['redirect'], 'utf-8'))

    def Update_App_Name(self):
        self.request.session['arbuz_app'] = self.app_name

    def Update_Notifications(self):

        today = datetime.today()
        deadlines = SQL.Filter(Order_Deadline, deadline__lt=today)
        reminders = SQL.Filter(Order_Deadline, reminder__lt=today)

        for deadline in deadlines:
            try: SQL.Save(Notification_Model,
                          name=deadline.name,
                          type='deadline',
                          date=today,
                          direct_url='{0}'.format(deadline.payment.pk))
            except: pass

        for reminder in reminders:
            try: SQL.Save(Notification_Model,
                          name=reminder.name,
                          type='reminder',
                          date=today,
                          direct_url='{0}'.format(reminder.payment.pk))
            except: pass

        self.request.session['notification_is_unreaded'] = \
            True if SQL.Filter(Notification_Model, not_viewed=True) \
                else False

    def __init__(self, _object):
        Base_Website.__init__(self, _object)
        self.length_navigation = None
        self.only_root = False
        self.authorization = False
        self.other_value = None
