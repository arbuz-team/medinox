from server.manage.switch.website.endpoints import *


class Ground_Block(Endpoints):

    def Manage_Content(self):
        return self.Render_HTML('block/menu_standard.html')

    def Error(self, response_class, context):
        return response_class(self.Render_To_String(
            'error/ground.html', context=context))
