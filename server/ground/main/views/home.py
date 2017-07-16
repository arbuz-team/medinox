from server.manage.switch.website.manager import *
from server.service.searcher.views import *


class Home(Website_Manager):

    def Manage_Content_Ground(self):
        self.Get_Post_Value('')
        self.content['recommended'] = SQL.Filter(Product,
            pk__in=SQL.All(Recommended_Product).values('product__pk'))

        return self.Render_HTML('main/start.html')

    @staticmethod
    def Launch(request):
        return Home(request).HTML
