from server.dialog.service.base import *
from server.manage.switch.position import *
from server.ground.main.models import *
from server.ground.product.forms import *


class Service_Home(Base_Service):

    def New(self, direction):

        # empty table
        if not self.dialog.Get_Post_Other('index'):
            home = Model_Home_Content(position=1)
            home.direction = Direction.DOWN
            self.request.session['main_home'] = \
                home

            return

        # get position parent
        index = self.dialog.Get_Post_Other('index')
        position = SQL.Get(Model_Home_Content, pk=index).position

        # create new
        home = Model_Home_Content(position=position)
        home.direction = direction
        self.request.session['main_home'] = home

    def Edit(self):

        home = SQL.Get(Model_Home_Content,
            pk=self.request.POST['value'])

        self.request.session['main_home'] = home
        self.context['image'] = home.image
        self.initial = {
            'header': home.header,
            'paragraph': home.paragraph,
        }

    def Not_Valid(self):
        self.context['title'] = Text(self, 93)
        return self.Render_Dialog(
            'prompt.html', 'home', only_root=True)

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
            'prompt.html', 'home', only_root=True)
