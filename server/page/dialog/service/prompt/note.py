from server.page.dialog.service.base import *


class Service_Note(Base_Service):

    def Edit(self):

        # open edit note
        if 'dialog_value' in self.request.POST:
            payment = self.request.POST['dialog_value']
            self.instance = Order_Note.objects.get(payment=payment)

        # when form not valid
        else: self.instance = \
            self.request.session['root_note']

    def Manage(self):

        # always edit
        self.Edit()

        self.request.session['root_note'] = self.instance
        self.content['form'] = Form_Order_Note(
            self.request, initial={'note': self.instance.note})

        self.content['title'] = Text(self.request, 172)
        return self.dialog.Render_Dialog(
            'dialog/prompt.html', 'note', only_root=True)
