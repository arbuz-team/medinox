from server.dialog.service.base import *
from server.service.payment.forms import *


class Service_Deadline(Base_Service):

    def Edit(self):

        # open edit deadline
        if 'value' in self.request.POST:
            payment = self.request.POST['value']
            self.instance = SQL.Get(Model_Deadline, payment=payment)

        # when form not valid
        else: self.instance = \
            self.request.session['root_deadline']

    def Not_Valid(self):
        pass

    def Manage(self):

        # always edit
        self.Edit()

        self.request.session['root_deadline'] = self.instance
        self.context['form'] = Form_Order_Deadline(
            self, instance=self.instance)

        self.context['title'] = Text(self, 171)
        return self.Render_Dialog(
            'deadline.html', 'deadline', only_root=True)

