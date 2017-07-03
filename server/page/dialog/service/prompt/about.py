from server.page.dialog.service.base import *


class Service_About(Base_Service):

    def Validate_Direction(self):
        direction = self.dialog\
            .Get_Post_Value('direction')

        switch = {
            'up':   Direction.UP,
            'down': Direction.DOWN,
            '':     None
        }

        self.direction = switch[direction]
        if self.direction:
            return True

        return False

    def New(self):

        # get position parent
        index = self.dialog.Get_Post_Value('index')
        position = About_Content.objects\
            .get(pk=index).position

        # create new
        about = About_Content(position=position)
        about.direction = self.direction
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

        if self.Validate_Direction():
            self.New()

        elif 'dialog_value' in self.request.POST:
            self.Edit()

        self.content['title'] = Text(self.request, 93)
        self.content['form'] = self.Prepare_Form(
            Form_About_Content, initial=self.initial)

        return self.Render_Dialog(
            'prompt.html', 'about', only_root=True)
