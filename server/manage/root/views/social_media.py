from server.manage.switch.website.manager import *
from server.manage.root.forms import *
from server.service.payment.forms import *


class Social_Media_Manager(Website_Manager):

    def Manage_Content(self):
        self.context['social_media'] = SQL.All(Model_Social_Media)
        return self.Render_HTML('root/social_media.html')

    def Manage_Form(self):

        pk = self.request.POST['_name_']
        url = self.request.POST['value']

        social = SQL.Get(Model_Social_Media, pk=pk)
        social.url = url
        SQL.Save(data=social)

        return HttpResponse()

    @staticmethod
    def Launch(request):
        return Social_Media_Manager(request, only_root=True).HTML
