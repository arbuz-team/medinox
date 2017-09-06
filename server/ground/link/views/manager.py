from server.manage.switch.website import *


class Link_Manager(Website_Manager):

    def Manage_Content(self):
        return self.Render_HTML('catalog/catalogs.html')

    @staticmethod
    def Launch(request):
        return Link_Manager(request, only_root=True).HTML
