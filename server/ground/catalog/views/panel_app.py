from server.ground.product.views import *


class Panel_App(Website_Manager):

    def Manage_Content_Ground(self):
        return self.Render_HTML('catalog/start.html')

    @staticmethod
    def Launch(request):
        return Panel_App(request).HTML
