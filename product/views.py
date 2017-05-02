from arbuz.views import *
from searcher.views import Search_Engine
from product.forms import *


class Start_App(Dynamic_Event_Manager):

    def Manage_Content_Ground(self):
        return self.Render_HTML('product/start.html')

    @staticmethod
    def Launch(request):
        return Start_App(request).HTML



class Details(Dynamic_Event_Manager):

    def Manage_Content_Ground(self):
        return self.Render_HTML('product/start.html')

    @staticmethod
    def Launch(request):
        return Details(request).HTML

