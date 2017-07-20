from server.dialog.service.base import *
from server.manage.switch.position import *


class Service_About(Base_Service):

    def New(self, direction):

        # get position parent
        index = self.dialog.Get_Post_Other('index')
        position = About_Content.objects\
            .get(pk=index).position

        # create new
        about = About_Content(position=position)
        about.direction = direction
        self.request.session['main_about'] = about

    def Edit(self):

        about = SQL.Get(About_Content,
            pk=self.request.POST['value'])

        self.request.session['main_about'] = about
        self.context['edit'] = {'url': '/product/description/manage/'}
        self.context['image'] = about.image
        self.initial = {
            'header': about.header,
            'paragraph': about.paragraph,
        }

    def Manage(self):

        position_manager = Position_Manager(self)
        direction = position_manager.Get_Direction()

        if direction:
            self.New(direction)

        elif 'value' in self.request.POST:
            self.Edit()

        self.context['title'] = Text(self, 93)
        self.context['form'] = self.Prepare_Form(
            Form_About_Content, initial=self.initial)

        return self.Render_Dialog(
            'prompt.html', 'about', only_root=True)
