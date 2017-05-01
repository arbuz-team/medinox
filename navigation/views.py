from arbuz.views import *


class Navigation(Dynamic_Event_Manager):

    def Manage_Content_Ground(self):
        pass

    def Manage_Content_Header(self):
        return self.Render_HTML('navigation/header.html')

    def Manage_Content_Navigation(self):
        return self.Render_HTML('navigation/navigation.html')

    def Manage_Content(self):

        if self.request.POST['__content__'] == 'header':
            return self.Manage_Content_Header()

        if self.request.POST['__content__'] == 'navigation':
            return self.Manage_Content_Navigation()

        self.content['error'] = 'no_event'
        return self.Render_HTML('arbuz/error.html')

    @staticmethod
    def Launch(request):
        return Navigation(request).HTML