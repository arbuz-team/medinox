from server.page.dialog.service.base import *


class Service_Deadline(Base_Service):

    def Edit(self):

        # open edit deadline
        if 'dialog_value' in self.request.POST:
            payment = self.request.POST['dialog_value']
            self.instance = Order_Deadline.objects.get(payment=payment)

        # when form not valid
        else: self.instance = \
            self.request.session['root_deadline']

    def Manage(self):

        # always edit
        self.Edit()

        self.request.session['root_deadline'] = self.instance
        self.content['form'] = Form_Order_Deadline(
            self.request, instance=self.instance)

        self.content['title'] = Text(self.request, 171)
        return self.dialog.Render_Dialog(
            'dialog/prompt.html', 'deadline', only_root=True)

