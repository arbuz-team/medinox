from server.service.sender.views import *
from server.manage.user.forms import *
import os, binascii


class Sign_Up(Website_Manager):

    def Manage_Content_Ground(self):
        self.content['form'] = Form_Register(self)
        return self.Render_HTML('user/sign_up.html', 'register')

    def Manage_Form_Register(self):
        self.content['form'] = Form_Register(self, post=True)

        if self.content['form'].is_valid():
            user = self.content['form'].save(commit=False)
            user.unique = User.Generate_User_Unique()
            SQL.Save(data=user)

            self.Create_No_Approved_User()
            self.Send_Activate_Link()

            self.content['form'] = Form_User_Address(self)
            return self.Render_HTML('user/sign_up.html', 'user_address')

        return self.Render_HTML('user/sign_up.html', 'register')

    def Manage_Form_User_Address(self):
        self.content['form'] = Form_User_Address(self, post=True)

        if self.content['form'].is_valid():
            address_user = self.content['form'].save(commit=False)
            address_user.user = self.request.session['user_user']
            SQL.Save(data=address_user)  # create address_user

            self.content['form'] = None  # message of correct
            return self.Render_HTML('user/sign_up.html')

        return self.Render_HTML('user/sign_up.html', 'user_address')

    def Manage_Form(self):

        if self.request.POST['__form__'] == 'register':
            return self.Manage_Form_Register()

        if self.request.POST['__form__'] == 'user_address':
            return self.Manage_Form_User_Address()

        return Website_Manager.Manage_Form(self)

    def Manage_Exist(self):

        if self.request.POST['__exist__'] == 'email':
            if SQL.Filter(User, email=self.request.POST['value']):
                return JsonResponse({'__exist__': 'true'})

        return JsonResponse({'__exist__': 'false'})

    def Create_No_Approved_User(self):
        self.content['key'] = binascii.hexlify(os.urandom(20))
        form = self.content['form']

        if not SQL.Filter(No_Approved_User, approved_key=self.content['key']):
            SQL.Save(No_Approved_User,
                user=SQL.Get(User, email=form.cleaned_data['email']),
                approved_key=self.content['key']
            )

        else: self.Create_No_Approved_User()

    def Send_Activate_Link(self):

        email = self.content['form'].cleaned_data['email']
        activate_key = self.content['key'].decode("utf-8")

        path_manager = Path_Manager(self)
        activate_url = path_manager.Get_Urls('user.approved',
                 {'key': activate_key}, current_language=True)

        content = {
            'activate_url': activate_url,
            'user':         self.request.session['user_user']
        }

        Sender(self.request).Send_Register_Approved_Link(content, email)

    @staticmethod
    def Launch(request):
        return Sign_Up(request).HTML
