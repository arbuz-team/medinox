from server.page.dialog.service.base import *
from server.manage.switch.module.position import *


class Service_About(Base_Service):

    def New(self, direction):

        # get position parent
        index = self.dialog.Get_Post_Value('index')
        position = About_Content.objects\
            .get(pk=index).position

        # create new
        about = About_Content(position=position)
        about.direction = direction
        self.request.session['main_about'] = about

    def Edit(self):

        about = About_Content.objects.get(
            pk=self.request.POST['dialog_value'])

        self.request.session['main_about'] = about
        self.content['edit'] = {'url': '/product/description/manage/'}
        self.content['image'] = about.image
        self.initial = {
            'header': about.header,
            'paragraph': about.paragraph,
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
            Form_About_Content, initial=self.initial)

        return self.Render_Dialog(
            'prompt.html', 'about', only_root=True)
