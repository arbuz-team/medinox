from server.manage.user.forms import *


class Panel_App(Website_Manager):

    def Manage_Content(self):

        path_manager = Path_Manager(self)
        self.content['apps'] = [
            {
                'name': Text(self, 35),
                'url':  path_manager.Get_Path('user.sign_in', current_language=True),
                'icon': '/static/img/icons/128/dark/padlock_open.png',
            },
            {
                'name': Text(self, 36),
                'url': path_manager.Get_Path('user.sign_up', current_language=True),
                'icon': '/static/img/icons/128/dark/moustache.png',
            },
            {
                'name': Text(self, 37),
                'url': path_manager.Get_Path('user.sign_out', current_language=True),
                'icon': '/static/img/icons/128/dark/logout.png',
            },
            {
                'name': Text(self, 38),
                'url': path_manager.Get_Path('user.account', current_language=True),
                'icon': '/static/img/icons/128/dark/settings.png',
            },
        ]

        return self.Render_HTML('arbuz/panel_app.html')

    @staticmethod
    def Launch(request):
        return Panel_App(request).HTML
