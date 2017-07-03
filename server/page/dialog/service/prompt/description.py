from server.page.dialog.service.base import *


class Service_Description(Base_Service):

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
        position = Description.objects\
            .get(pk=index).position

        # create new description
        description = Description()
        self.request.session['product_description'] = description
        self.dialog.Add_Model_Order(Description, description,
                                    position, self.direction)

    def Edit(self):

        description = Description.objects.get(
            pk=self.request.POST['dialog_value'])

        self.request.session['product_description'] = description
        self.content['edit'] = {'url': '/product/description/manage/'}
        self.content['image'] = description.image
        self.instance = {
            'header': description.header,
            'paragraph': description.paragraph,
        }

    def Manage(self):

        if self.Validate_Direction():
            self.New()

        elif 'dialog_value' in self.request.POST:
            self.Edit()

        self.content['title'] = Text(self.request, 93)
        self.content['form'] = self.Prepare_Form(
            Form_Description, initial=self.instance)

        return self.Render_Dialog(
            'prompt.html', 'description', only_root=True)

