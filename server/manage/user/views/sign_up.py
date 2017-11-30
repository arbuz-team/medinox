from server.service.sender.views import *
from server.manage.user.forms import *


class Sign_Up(Website_Manager):

    def Manage_Content(self):
        self.context['form'] = Form_Register(self)
        return self.Render_HTML('user/sign_up_step_1.html', 'register')

    def Manage_Form_Register(self):
        self.context['form'] = Form_Register(self, post=True)

        if self.context['form'].is_valid():
            user = self.context['form'].save(commit=False)
            user.unique = Model_User.Generate_User_Unique()
            SQL.Save(data=user)

            self.Create_No_Approved_User()
            self.Send_Activate_Link()

            self.request.session['user_user'] = user
            self.context['form'] = Form_User_Address(self)
            return self.Render_HTML('user/sign_up_step_2.html', 'user_address')

        return self.Render_HTML('user/sign_up_step_1.html', 'register')

    def Manage_Form_User_Address(self):
        self.context['form'] = Form_User_Address(self, post=True)

        if self.context['form'].is_valid():
            address_user = self.context['form'].save(commit=False)
            address_user.user = self.request.session['user_user']
            SQL.Save(data=address_user)  # create address_user

            self.context['form'] = None  # message of correct
            return self.Render_HTML('user/sign_up_step_2.html')

        return self.Render_HTML('user/sign_up_step_2.html', 'user_address')

    def Manage_Form(self):

        if self.request.POST['_name_'] == 'register':
            return self.Manage_Form_Register()

        if self.request.POST['_name_'] == 'user_address':
            return self.Manage_Form_User_Address()

        return Website_Manager.Manage_Form(self)

    def Manage_Exist(self):

        if self.request.POST['_name_'] == 'email':
            if SQL.Filter(Model_User, email=self.request.POST['value']):
                return HttpResponse('true')

        if self.request.POST['_name_'] == 'password':
            path = './server/manage/user/passwords'
            passwords = open(Path_Manager.Base_Root(path)).read()

            if self.request.POST['value'] in passwords.splitlines():
                return HttpResponse('true')

        return HttpResponse('false')

    def Create_No_Approved_User(self):

        form = self.context['form']
        self.context['key'] = self.Generate_Random_Chars(
            20, punctuation=False, uppercase=False)

        if not SQL.Filter(Model_No_Approved_User, approved_key=self.context['key']):
            email = form.cleaned_data['email']
            user = SQL.Get(Model_User, email=email)

            SQL.Save(Model_No_Approved_User,
                user=user,
                approved_key=self.context['key']
            )

        else: self.Create_No_Approved_User()

    def Send_Activate_Link(self):

        email = self.context['form'].cleaned_data['email']
        activate_key = self.context['key']

        path_manager = Path_Manager(self)
        activate_url = path_manager.Get_Urls('user.approved',
             {'key': activate_key}, current_language=True)

        content = {
            'activate_url': activate_url,
            'user':         self.request.session['user_user']
        }

        Sender(self).Send_Register_Approved_Link(content, email)

    @staticmethod
    def Launch(request):
        return Sign_Up(request).HTML
