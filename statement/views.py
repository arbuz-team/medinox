from arbuz.views import *


class Statement_403(Dynamic_Event_Manager):

    def Manage_Content_Ground(self):
        self.content['title'] = '403'
        return self.Render_HTML('statement/statement.html')

    @staticmethod
    def Launch(request):
        return Statement_403(request).HTML



class Statement_404(Dynamic_Event_Manager):

    def Manage_Content_Ground(self):
        self.content['title'] = '404'
        return self.Render_HTML('statement/statement.html')

    @staticmethod
    def Launch(request):
        return Statement_404(request).HTML



class Statement_500(Dynamic_Event_Manager):

    def Manage_Content_Ground(self):
        self.content['title'] = '500'
        return self.Render_HTML('statement/statement.html')

    @staticmethod
    def Launch(request):
        return Statement_500(request).HTML
