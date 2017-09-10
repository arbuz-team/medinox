from server.manage.user.forms import *


class Sign_In(Website_Manager):

    def Manage_Content(self):
        self.context['form'] = Form_Login(self)
        return self.Render_HTML('user/sign_in.html', 'login')

    def Manage_Form_Login(self):
        self.context['form'] = Form_Login(self, post=True)

        if self.context['form'].is_valid():
            email = self.context['form'].cleaned_data['email']
            unique = SQL.Get(Model_User, email=email).unique

            self.request.session['user_login'] = True
            self.request.session['user_user'] = \
                SQL.Get(Model_User, unique=unique)

            self.context['form'] = None  # message of correct
            return self.Render_HTML('user/sign_in.html')

        return self.Render_HTML('user/sign_in.html', 'login')

    def Manage_Form(self):

        if self.request.POST['_name_'] == 'login':
            return self.Manage_Form_Login()

        return Website_Manager.Manage_Form(self)

    @staticmethod
    def Redirect(request, url):
        other_value = {'redirect': url}
        return Sign_In(request, other_value=other_value,
                       length_navigation=2).HTML

    @staticmethod
    def Launch(request):
        return Sign_In(request).HTML



class Sign_In_Cart(Sign_In):

    def Manage_Form(self):
        self.context['form'] = Form_Login(self, post=True)

        if self.context['form'].is_valid():
            email = self.context['form'].cleaned_data['email']
            unique = SQL.Get(Model_User, email=email).unique

            self.request.session['user_login'] = True
            self.request.session['user_user'] = \
                SQL.Get(Model_User, unique=unique)

            self.context['form'] = None  # message of correct
            self.context['cart_open'] = True
            return self.Render_HTML('user/sign_in.html')

        return self.Render_HTML('user/sign_in.html', 'login')

    @staticmethod
    def Launch(request):
        return Sign_In_Cart(request).HTML

