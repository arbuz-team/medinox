from server.dialog.service.base import *
from server.manage.switch.position import *
from server.ground.product.forms import *


class Service_Description(Base_Service):

    def New(self, direction):

        # empty table
        if not self.dialog.Get_Post_Other('index'):

            description = Model_Description(position=1)
            description.direction = Direction.DOWN
            self.request.session['product_description'] = \
                description

            return

        # get position parent description
        index = self.dialog.Get_Post_Other('index')
        position = SQL.Get(Model_Description, pk=index).position

        # create new description
        description = Model_Description(position=position)
        description.direction = direction
        self.request.session['product_description'] = description

    def Edit(self):

        description = SQL.Get(Model_Description,
            pk=self.request.POST['value'])

        self.request.session['product_description'] = description
        self.context['edit'] = {'url': '/product/description/manage/'}
        self.context['image'] = description.image
        self.initial = {
            'header': description.header,
            'paragraph': description.paragraph,
        }

    def Not_Valid(self):
        self.context['title'] = Text(self, 93)
        return self.Render_Dialog(
            'prompt.html', 'description', only_root=True)

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
            'prompt.html', 'description', only_root=True)

