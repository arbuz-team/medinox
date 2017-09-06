from server.dialog.service.base import *


class Service_Note(Base_Service):

    def Edit(self):

        # open edit note
        if 'value' in self.request.POST:
            payment = self.request.POST['value']
            self.instance = SQL.Get(Model_Order_Note, payment=payment)

        # when form not valid
        else: self.instance = \
            self.request.session['root_note']

    def Manage(self):

        # always edit
        self.Edit()

        self.request.session['root_note'] = self.instance
        self.context['form'] = Form_Order_Note(
            self, initial={'note': self.instance.note})

        self.context['title'] = Text(self, 172)
        return self.Render_Dialog(
            'prompt.html', 'note', only_root=True)
