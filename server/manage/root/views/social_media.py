from server.manage.switch.website.manager import *
from server.manage.root.forms import *
from server.service.payment.forms import *


class Social_Media_Manager(Website_Manager):

    def Manage_Content(self):
        self.content['social_media'] = SQL.All(Social_Media)
        return self.Render_HTML('root/social_media.html')

    def Manage_Form(self):

        pk = self.request.POST['__form__']
        url = self.request.POST['value']

        social = SQL.Get(Social_Media, pk=pk)
        social.url = url
        SQL.Save(data=social)

        return JsonResponse({'__form__': 'true'})

    @staticmethod
    def Launch(request):
        return Social_Media_Manager(request, only_root=True).HTML
