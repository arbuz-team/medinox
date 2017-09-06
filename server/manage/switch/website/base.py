from server.service.file.views import *
from server.manage.switch.paths import *
from server.manage.switch.status import *
from server.manage.switch.settings import *
from server.service.sql.views import *
from server.service.translator.views import *


class Base_Website(Base):

    def Get_Post_Other(self, name):

        for key in self.request.POST.keys():

            # only other values
            if 'other_' in key:
                value = self.request.POST[key]

                # name:value
                if value.split(':')[0] == name:
                    return value.split(':')[1]

        # not found
        return ''

    def Validate_Period(self, session_name_date_from, session_name_date_to):

        date_from = self.request.session[session_name_date_from]
        date_to = self.request.session[session_name_date_to]

        # valid if string convert to date
        try: datetime.strptime(date_from, '%Y-%m-%d')
        except ValueError:
            self.request.session[session_name_date_from] = \
                (datetime.today() - timedelta(days=7)).strftime('%Y-%m-%d')

        # valid if string convert to date
        try: datetime.strptime(date_to, '%Y-%m-%d')
        except ValueError:
            self.request.session[session_name_date_to] = \
                datetime.today().strftime('%Y-%m-%d')

        # valid period
        if date_from > date_to:
            self.request.session[session_name_date_from] = \
                self.request.session[session_name_date_to]

    def Clear_Session(self, key_contain=''):

        keys = list(self.request.session.keys())
        for key in keys:
            if key_contain in key:
                del self.request.session[key]

    @staticmethod
    def Encrypt(password):
        return make_password(password=password, salt='arbuz-team')

    def __init__(self, _object):
        Base.__init__(self, _object)

        self.start_time = 0
        self.context = {}

        self.app_name = self.__module__.rsplit('.', 1)[0]
        self.short_app_name = self.app_name.rsplit('.', 1)[1]

