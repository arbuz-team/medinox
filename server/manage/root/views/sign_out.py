from server.manage.switch.website.manager import *

class Sign_Out(Website_Manager):

    def Manage_Content_Ground(self):
        self.request.session['root_login'] = False
        self.request.session['product_number_product_on_page'] = 10
        return self.Render_HTML('root/sign_out.html')

    def Check_Authorization(self):

        if self.authorization:
            if self.request.session['root_login']:
                return True

        else: return True
        return False

    @staticmethod
    def Launch(request):
        return Sign_Out(request, only_root=True).HTML
