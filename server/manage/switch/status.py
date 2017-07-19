from server.manage.switch.paths import *


class Status_Manager(Base):

    @staticmethod
    def Get_Text_Cell(text, spaces=20, margin=0):
        spaces = ' ' * (spaces - len(text) - margin)
        margin = ' ' * margin
        return margin + text + spaces

    @staticmethod
    def Get_Text_Value(value):
        if len(str(value)) > 100:
            return str(value)[:100] + ' ...'

        return str(value)[:100]

    def Timer_Start(self):
        if DISPLAY_STATUS:
            self.start_time = time.time()

    def Add_App_Name(self, message):

        if not self.app_name:
            return

        self.status += self.Get_Text_Cell('Application: ')
        self.status += self.Get_Text_Value(self.app_name)

        if message: self.status += ' ({0}) \n\n'.format(message)
        else: self.status += '\n\n'

    def Add_Method_Name(self):
        self.status += self.Get_Text_Cell('Method: ', margin=2)
        self.status += self.Get_Text_Value(self.request.method) + '\n'

    def Add_Duration(self):
        duration = time.time() - self.start_time
        duration = str(int(duration * 1000))
        self.status += self.Get_Text_Cell('Duration: ', margin=2)
        self.status += self.Get_Text_Value(duration) + ' ms\n'

    def Add_URL(self):

        try:

            path_manager = Path_Manager(self)
            path = path_manager.Get_Path(current_language=True)

            self.status += self.Get_Text_Cell('URL: ', margin=2)
            self.status += self.Get_Text_Value(path) + '\n'

        except: pass

    def Add_HTTP_Variables(self, http_dict):

        if http_dict:
            variables = []

            # get post keys
            keys = http_dict.keys()
            keys = sorted(keys)

            # create print data
            for key in keys:
                variables.append(
                    self.Get_Text_Cell(key, 30) +
                    self.Get_Text_Value((http_dict[key]))
                )

            # empty line before and title
            title = self.request.method + ': '
            title = self.Get_Text_Cell(title, margin=2)
            self.status += '\n' + title

            # add variables
            separator = '\n' + self.Get_Text_Cell('')
            self.status += separator.join(variables) + '\n'

    def Add_Session_Variables(self):

        keys = self.request.session.keys()
        if any(key.startswith(self.short_app_name) for key in keys):

            keys = sorted(keys)
            variables = []

            for key in keys:
                if key.startswith(self.short_app_name):
                    variables.append(
                        self.Get_Text_Cell(key, 30) +
                        self.Get_Text_Value(self.request.session[key])
                    )

            # empty line before and title
            title = self.Get_Text_Cell('Session: ', margin=2)
            self.status += '\n' + title

            # add variables
            separator = '\n' + self.Get_Text_Cell('')
            self.status += separator.join(variables) + '\n'

    def Add_Variables(self):

        if self.request.method == 'POST':
            self.Add_HTTP_Variables(self.request.POST)

        if self.request.method == 'GET':
            self.Add_HTTP_Variables(self.request.GET)

        self.Add_Session_Variables()
        self.status += '\n' + '-' * 125 + '\n'

    def Display_Status(self, message=None):

        if not DISPLAY_STATUS and not message:
            return

        # main data
        self.Add_App_Name(message)
        self.Add_URL()
        self.Add_Method_Name()
        self.Add_Duration()

        # variables
        self.Add_Variables()

        # print
        print(self.status)

    def __init__(self, _object):
        Base.__init__(self, _object)

        self.app_name = ''
        self.short_app_name = ''
        self.start_time = 0
        self.status = '-' * 125 + '\n\n'

        try:

            self.app_name = _object.app_name
            self.short_app_name = _object.short_app_name

        except: pass
