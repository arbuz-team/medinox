from server.manage.switch.website.manager import *


class Panel_App(Website_Manager):

    def Manage_Content(self):

        path_manager = Path_Manager(self)
        self.content['apps'] = [
            {
                'name': Text(self, 58),
                'url':  path_manager.Get_Path('user.account.details', current_language=True),
                'icon': '/static/img/icons/128/dark/user_details.png',
            },
            {
                'name': Text(self, 59),
                'url': path_manager.Get_Path('user.account.addresses', current_language=True),
                'icon': '/static/img/icons/128/dark/id_card.png',
            },
            {
                'name': Text(self, 60),
                'url': path_manager.Get_Path('user.account.my_shopping', current_language=True),
                'icon': '/static/img/icons/128/dark/list_check.png',
            },
            {
                'name': Text(self, 61),
                'url': path_manager.Get_Path('user.account.favorite', current_language=True),
                'icon': '/static/img/icons/128/dark/badge.png',
            },
            {
                'name': Text(self, 62),
                'url': path_manager.Get_Path('payment', current_language=True),
                'icon': '/static/img/icons/128/dark/shopping_cart.png',
            },
        ]

        return self.Render_HTML('arbuz/panel_app.html')

    @staticmethod
    def Launch(request):
        return Panel_App(request, authorization=True).HTML
