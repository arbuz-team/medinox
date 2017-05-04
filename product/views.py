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
        self.content['product'] = Product.objects.get(pk=self.other_value)
        return self.Render_HTML('product/details.html')

    @staticmethod
    def Details(request, pk):
        return Details(request, other_value=pk).HTML

    @staticmethod
    def Launch(request):
        pass

