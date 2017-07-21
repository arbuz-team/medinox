from server.manage.switch.website.endpoints import *


class Menu_Mobile_Block(Endpoints):

    def Manage_Content(self):
        return self.Render_HTML('block/menu.html')

    def Error(self, response_class, context):
        return response_class(self.Render_To_String(
            'error/menu.html', context=context))
