from server.manage.switch.website.endpoints import *


class Ground_Block(Endpoints):

    def Error(self, response_class, context):
        return response_class(self.Render_To_String(
            'error/ground.html', context=context))
