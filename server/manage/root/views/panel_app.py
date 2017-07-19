from server.manage.switch.website.manager import *
from server.service.payment.forms import *


class Panel_App(Website_Manager):

    def Manage_Content(self):

        path_manager = Path_Manager(self)
        self.context['apps'] = [
            {
                'name': Text(self, 24),
                'url': path_manager.Get_Path('root.sign_out', current_language=True),
                'icon': '/static/img/icons/128/dark/logout.png',
            },
            {
                'name': Text(self, 25),
                'url': path_manager.Get_Path('root.company_details', current_language=True),
                'icon': '/static/img/icons/128/dark/moustache.png',
            },
            {
                'name': Text(self, 27),
                'url': path_manager.Get_Path('root.users_payments', current_language=True),
                'icon': '/static/img/icons/128/dark/money.png',
            },
            {
                'name': Text(self, 135),
                'url': path_manager.Get_Path('root.social_media', current_language=True),
                'icon': '/static/img/icons/128/dark/social_group.png',
            },
            {
                'name': Text(self, 136),
                'url': path_manager.Get_Path('root.delivery_settings', current_language=True),
                'icon': '/static/img/icons/128/dark/transport.png',
            },
        ]

        return self.Render_HTML('arbuz/panel_app.html')

    @staticmethod
    def Launch(request):
        return Panel_App(request, only_root=True).HTML
