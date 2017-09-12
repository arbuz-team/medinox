from server.dialog.service.base import *
from server.manage.root.forms import *


class Service_Send_Email(Base_Service):

    def Open_Dialog(self):

        if 'value' in self.request.POST:
            payment = self.request.POST['value']
            self.request.session['root_payment'] = \
                SQL.Get(Model_Payment, pk=payment)

    def Not_Valid(self):
        pass

    def Manage(self):

        self.Open_Dialog()
        self.context['title'] = Text(self, 172)
        self.context['form'] = Form_Send_Email(self)

        return self.Render_Dialog(
            'prompt.html', 'send_email', only_root=True)
