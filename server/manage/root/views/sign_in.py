from server.manage.switch.website.manager import *
from server.manage.root.forms import *


class Sign_In(Website_Manager):

    def Manage_Content(self):
        self.content['form'] = Form_Root_Login(self)
        return self.Render_HTML('root/sign_in.html', 'login')

    def Manage_Form_Login(self):
        self.content['form'] = Form_Root_Login(self, post=True)

        if self.content['form'].is_valid():
            self.request.session['root_login'] = True
            self.request.session['product_number_product_on_page'] = 9

            self.content['form'] = None  # message of correct
            return self.Render_HTML('root/sign_in.html')

        return self.Render_HTML('root/sign_in.html', 'login')

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
