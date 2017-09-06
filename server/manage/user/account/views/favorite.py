from server.manage.switch.website.manager import *
from server.manage.user.account.forms import *
from server.service.payment.models import *


class Favorite(Website_Manager):

    def Manage_Content(self):
        user = self.request.session['user_user']
        self.context['elements'] = SQL.Filter(Model_Product,
            pk__in=SQL.Filter(Model_Favorite_Product, user=user).values('product__pk'))

        return self.Render_HTML('user/account/favorite.html')

    @staticmethod
    def Launch(request):
        return Favorite(request, authorization=True).HTML
