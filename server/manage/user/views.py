from server.manage.switch.views import *
from server.service.sender.views import *
from server.manage.user.forms import *
import os, binascii


class Start_App(Dynamic_Event_Manager):

    def Manage_Content_Ground(self):

        path_manager = Path_Manager(self)
        self.content['apps'] = [
            {
                'name': Text(self, 35),
                'url':  path_manager.Get_Path('user.sign_in', current_language=True),
                'icon': '/static/img/icons/128/dark/padlock_open.png',
            },
            {
                'name': Text(self, 36),
                'url': path_manager.Get_Path('user.sign_up', current_language=True),
                'icon': '/static/img/icons/128/dark/moustache.png',
            },
            {
                'name': Text(self, 37),
                'url': path_manager.Get_Path('user.sign_out', current_language=True),
                'icon': '/static/img/icons/128/dark/logout.png',
            },
            {
                'name': Text(self, 38),
                'url': path_manager.Get_Path('user.account', current_language=True),
                'icon': '/static/img/icons/128/dark/settings.png',
            },
        ]

        return self.Render_HTML('arbuz/start_app.html')

    @staticmethod
    def Launch(request):
        return Start_App(request).HTML



class Sign_In(Dynamic_Event_Manager):

    def Manage_Content_Ground(self):
        self.content['form'] = Form_Login(self.request)
        return self.Render_HTML('user/sign_in.html', 'login')

    def Manage_Form_Login(self):

        self.content['form'] = \
            Form_Login(self.request, self.request.POST)

        if self.content['form'].is_valid():
            email = self.content['form'].cleaned_data['email']
            unique = User.objects.get(email=email).unique

            self.request.session['user_login'] = True
            self.request.session['user_unique'] = unique
            self.request.session['user_username'] = \
                User.objects.get(unique=unique).username

            self.content['form'] = None  # message of correct
            return self.Render_HTML('user/sign_in.html')

        return self.Render_HTML('user/sign_in.html', 'login')

    def Manage_Form(self):

        if self.request.POST['__form__'] == 'login':
            return self.Manage_Form_Login()

        return Dynamic_Event_Manager.Manage_Form(self)

    @staticmethod
    def Redirect(request, url):
        other_value = {'redirect': url}
        return Sign_In(request, other_value=other_value,
                       length_navigation=2).HTML

    @staticmethod
    def Launch(request):
        return Sign_In(request).HTML



class Sign_Up(Dynamic_Event_Manager):

    def Manage_Content_Ground(self):
        self.content['form'] = Form_Register(self.request)
        return self.Render_HTML('user/sign_up.html', 'register')

    def Manage_Form_Register(self):

        self.content['form'] = Form_Register(
            self.request, self.request.POST)

        if self.content['form'].is_valid():
            user = self.content['form'].save(commit=False)
            user.unique = User.Generate_User_Unique()
            self.request.session['user_unique'] = user.unique
            user.save()

            self.Create_No_Approved_User()
            self.Send_Activate_Link()

            self.content['form'] = Form_User_Address(self.request)
            return self.Render_HTML('user/sign_up.html', 'user_address')

        return self.Render_HTML('user/sign_up.html', 'register')

    def Manage_Form_User_Address(self):

        self.content['form'] = Form_User_Address(
            self.request, self.request.POST)

        if self.content['form'].is_valid():
            unique = self.request.session['user_unique']
            address_user = self.content['form'].save(commit=False)
            address_user.user = User.objects.get(unique=unique)
            address_user.save()  # create address_user

            self.content['form'] = None  # message of correct
            return self.Render_HTML('user/sign_up.html')

        return self.Render_HTML('user/sign_up.html', 'user_address')

    def Manage_Form(self):

        if self.request.POST['__form__'] == 'register':
            return self.Manage_Form_Register()

        if self.request.POST['__form__'] == 'user_address':
            return self.Manage_Form_User_Address()

        return Dynamic_Event_Manager.Manage_Form(self)

    def Manage_Exist(self):

        if self.request.POST['__exist__'] == 'email':
            if User.objects.filter(email=self.request.POST['value']):
                return JsonResponse({'__exist__': 'true'})

        return JsonResponse({'__exist__': 'false'})

    def Create_No_Approved_User(self):
        self.content['key'] = binascii.hexlify(os.urandom(20))
        form = self.content['form']

        if not No_Approved_User.objects.filter(approved_key=self.content['key']):
            No_Approved_User\
            (
                user=User.objects.get(email=form.cleaned_data['email']),
                approved_key=self.content['key']
            ).save()

        else: self.Create_No_Approved_User()

    def Send_Activate_Link(self):

        email = self.content['form'].cleaned_data['email']
        activate_key = self.content['key'].decode("utf-8")
        user_unique = self.request.session['user_unique']

        path_manager = Path_Manager(self)
        activate_url = path_manager.Get_Urls('user.approved',
                 {'key': activate_key}, current_language=True)

        content = {
            'activate_url': activate_url,
            'user':         User.objects.get(unique=user_unique)
        }

        Sender(self.request).Send_Register_Approved_Link(content, email)

    @staticmethod
    def Launch(request):
        return Sign_Up(request).HTML



class Sign_Out(Dynamic_Event_Manager):

    def Manage_Content_Ground(self):
        self.request.session['user_login'] = False
        self.request.session['user_unique'] = ''
        self.request.session['user_username'] = ''
        return self.Render_HTML('user/sign_out.html')

    @staticmethod
    def Launch(request):
        return Sign_Out(request, authorization=True).HTML



class Approved_Register(Dynamic_Event_Manager):

    def Manage_Content_Ground(self):
        return self.Render_HTML('user/approved.html')

    @staticmethod
    def Update_User_Status(request, key):
        all_keys = No_Approved_User.objects.values('approved_key')

        if {'approved_key': key} in all_keys:
            record = No_Approved_User.objects.get(approved_key=key)
            record.user.approved = True
            record.user.save()
            record.delete()

        return Approved_Register(request, length_navigation=2).HTML

    @staticmethod
    def Launch(request):
        return Approved_Register(request).HTML



class Forgot_Password(Dynamic_Event_Manager):

    def Manage_Content_Ground(self):
        self.content['form'] = Form_Forgot_Password(self.request)
        return self.Render_HTML('user/forgot.html', 'forgot_password')

    def Manage_Form_Forgot_Password(self):

        self.content['form'] = \
            Form_Forgot_Password(self.request, self.request.POST)

        if self.content['form'].is_valid():
            self.content['email'] = self.content['form'].cleaned_data['email']

            if User.objects.filter(email=self.content['email']):
                self.Create_Forgot_Password_User()
                self.Send_Secure_Link()

            self.content['form'] = None  # message of correct

            return self.Render_HTML('user/forgot.html')

        return self.Render_HTML('user/forgot.html', 'forgot_password')

    def Manage_Form(self):

        if self.request.POST['__form__'] == 'forgot_password':
            return self.Manage_Form_Forgot_Password()

        return Dynamic_Event_Manager.Manage_Form(self)

    def Create_Forgot_Password_User(self):
        self.content['key'] = binascii.hexlify(os.urandom(20))

        if not Forgot_Password_User.objects.filter(approved_key=self.content['key']):
            Forgot_Password_User\
            (
                user=User.objects.get(email=self.content['email']),
                approved_key=self.content['key']
            ).save()

        else: self.Create_Forgot_Password_User()

    def Send_Secure_Link(self):

        path_manager = Path_Manager(self)
        activate_key = self.content['key'].decode("utf-8")
        activate_url = path_manager.Get_Urls('user.change_password',
             kwargs={'key': activate_key}, current_language=True)

        email = self.content['email']

        content = {
            'activate_url': activate_url,
            'user':         User.objects.get(email=email)
        }

        Sender(self.request).Send_Forgot_Password_Link(content, email)

    def Manage_Exist(self):

        if self.request.POST['__exist__'] == 'email':
            if User.objects.filter(email=self.request.POST['value']):
                return JsonResponse({'__exist__': 'true'})

        return JsonResponse({'__exist__': 'false'})

    @staticmethod
    def Launch(request):
        return Forgot_Password(request).HTML



class Change_Password(Dynamic_Event_Manager):

    def Manage_Content_Ground(self):
        self.content['form'] = Form_Change_Password(self.request)
        return self.Render_HTML('user/change_password.html', 'change_password')

    def Manage_Form_Change_Password(self):

        self.content['form'] = \
            Form_Change_Password(self.request, self.request.POST)

        if self.content['form'].is_valid():

            key = self.other_value['key']
            record = Forgot_Password_User.objects.get(approved_key=key)
            record.user.password = self.content['form'].cleaned_data['password']
            record.user.save()
            record.delete()

            self.content['form'] = None  # message of correct

            return self.Render_HTML('user/change_password.html')

        return self.Render_HTML('user/change_password.html', 'change_password')

    def Manage_Form(self):

        if self.request.POST['__form__'] == 'change_password':
            return self.Manage_Form_Change_Password()

        return Dynamic_Event_Manager.Manage_Form(self)

    @staticmethod
    def Secure(request, key):
        all_keys = Forgot_Password_User.objects.values('approved_key')

        if {'approved_key': key} in all_keys:
            value = {'key': key}
            return Change_Password(request, other_value=value).HTML

        return Change_Password(request, error_method='Error_Authorization').HTML

    @staticmethod
    def Launch(request):
        return Change_Password(request).HTML



class User_Agreement(Dynamic_Event_Manager):

    def Manage_Content_Ground(self):
        return self.Render_HTML('user/agreement.html')

    @staticmethod
    def Launch(request):
        return User_Agreement(request).HTML
