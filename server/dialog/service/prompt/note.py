from server.dialog.service.base import *


class Service_Note(Base_Service):

    def Edit(self):

        # open edit note
        if 'dialog_value' in self.request.POST:
            payment = self.request.POST['dialog_value']
            self.instance = SQL.Get(Order_Note, payment=payment)

        # when form not valid
        else: self.instance = \
            self.request.session['root_note']

    def Manage(self):

        # always edit
        self.Edit()

        self.request.session['root_note'] = self.instance
        self.content['form'] = Form_Order_Note(
            self, initial={'note': self.instance.note})

        self.content['title'] = Text(self, 172)
        return self.Render_Dialog(
            'prompt.html', 'note', only_root=True)