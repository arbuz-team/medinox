from server.dialog.service.base import *
from server.manage.switch.position import *


class Service_Description(Base_Service):

    def New(self, direction):

        # get position parent description
        index = self.dialog.Get_Post_Value('index')
        position = Description.objects\
            .get(pk=index).position

        # create new description
        description = Description(position=position)
        description.direction = direction
        self.request.session['product_description'] = description

    def Edit(self):

        description = SQL.Get(Description,
            pk=self.request.POST['dialog_value'])

        self.request.session['product_description'] = description
        self.content['edit'] = {'url': '/product/description/manage/'}
        self.content['image'] = description.image
        self.initial = {
            'header': description.header,
            'paragraph': description.paragraph,
        }

    def Manage(self):

        position_manager = Position_Manager(self)
        direction = position_manager.Get_Direction()

        if direction:
            self.New(direction)

        elif 'dialog_value' in self.request.POST:
            self.Edit()

        self.content['title'] = Text(self, 93)
        self.content['form'] = self.Prepare_Form(
            Form_Description, initial=self.initial)

        return self.Render_Dialog(
            'prompt.html', 'description', only_root=True)

