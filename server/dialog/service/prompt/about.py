from server.dialog.service.base import *
from server.manage.switch.position import *
from server.ground.main.models import *
from server.ground.product.forms import *


class Service_About(Base_Service):

    def New(self, direction):

        # empty table
        if not self.dialog.Get_Post_Other('index'):
            about = Model_About_Content(position=1)
            about.direction = Direction.DOWN
            self.request.session['main_about'] = \
                about

            return

        # get position parent
        index = self.dialog.Get_Post_Other('index')
        position = SQL.Get(Model_About_Content, pk=index).position

        # create new
        about = Model_About_Content(position=position)
        about.direction = direction
        self.request.session['main_about'] = about

    def Edit(self):

        about = SQL.Get(Model_About_Content,
            pk=self.request.POST['value'])

        self.request.session['main_about'] = about
        self.context['image'] = about.image
        self.initial = {
            'header': about.header,
            'paragraph': about.paragraph,
        }

    def Not_Valid(self):
        self.context['title'] = Text(self, 93)
        return self.Render_Dialog(
            'prompt.html', 'about', only_root=True)

    def Manage(self):

        position_manager = Position_Manager(self)
        direction = position_manager.Get_Direction()

        if direction:
            self.New(direction)

        elif 'value' in self.request.POST:
            self.Edit()

        self.context['title'] = Text(self, 93)
        self.context['form'] = self.Prepare_Form(
            Form_Description, initial=self.initial)

        return self.Render_Dialog(
            'prompt.html', 'about', only_root=True)
