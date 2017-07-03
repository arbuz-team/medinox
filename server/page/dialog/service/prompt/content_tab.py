from server.page.dialog.service.base import *


class Service_Content_Tab(Base_Service):

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

        # get position parent description
        index = self.dialog.Get_Post_Value('index')
        position = Content_Tab.objects\
            .get(pk=index).position

        # create new description
        content_tab = Content_Tab(position=position)
        content_tab.direction = self.direction
        self.request.session['main_content_tab'] = content_tab

    def Edit(self):

        content_tab = Content_Tab.objects.get(
            pk=self.request.POST['dialog_value'])

        self.request.session['main_content_tab'] = content_tab
        self.content['edit'] = {'url': '/product/description/manage/'}
        self.content['image'] = content_tab.image
        self.initial = {
            'header': content_tab.header,
            'paragraph': content_tab.paragraph,
        }

    def Manage(self):

        if self.Validate_Direction():
            self.New()

        elif 'dialog_value' in self.request.POST:
            self.Edit()

        self.content['title'] = Text(self.request, 93)
        self.content['form'] = self.Prepare_Form(
            Form_Content_Tab, initial=self.initial)

        return self.Render_Dialog(
            'prompt.html', 'content_tab', only_root=True)
