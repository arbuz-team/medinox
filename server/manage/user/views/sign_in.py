from server.manage.user.forms import *


class Sign_In(Website_Manager):

    def Manage_Content_Ground(self):
        self.content['form'] = Form_Login(self)
        return self.Render_HTML('user/sign_in.html', 'login')

    def Manage_Form_Login(self):
        self.content['form'] = Form_Login(self, post=True)

        if self.content['form'].is_valid():
            email = self.content['form'].cleaned_data['email']
            unique = SQL.Get(User, email=email).unique

            self.request.session['user_login'] = True
            self.request.session['user_user'] = \
                SQL.Get(User, unique=unique)

            self.content['form'] = None  # message of correct
            return self.Render_HTML('user/sign_in.html')

        return self.Render_HTML('user/sign_in.html', 'login')

    def Manage_Form(self):

        if self.request.POST['__form__'] == 'login':
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
