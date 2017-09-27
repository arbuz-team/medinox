from server.service.payment.forms import *
from server.service.sender.views import *
from server.manage.root.forms import *


class Users_Payments(Website_Manager):

    def Get_Date(self):

        date_from = self.request.session['root_users_payments_date_from']
        date_from = datetime.strptime(date_from, '%Y-%m-%d')
        date_to = self.request.session['root_users_payments_date_to']
        date_to = datetime.strptime(date_to, '%Y-%m-%d')

        return date_from, date_to

    def Create_Payment_Structure(self):

        self.context['shopping'] = []

        date_from, date_to = self.Get_Date()
        status = self.request.session['root_payment_status']
        payments = SQL.Filter(Model_Payment, status=status,
                      date__gte=date_from, date__lte=date_to)

        for payment in payments:

            details = {
                'name': SQL.Get(Model_Invoice_Address, payment=payment).name,
                'surname': SQL.Get(Model_Invoice_Address, payment=payment).surname,
                'company_name': SQL.Get(Model_Invoice_Address, payment=payment).company_name,
                'payment':  payment,
                'products': SQL.Filter(Model_Payment_Product, payment=payment)
            }

            self.context['shopping'].append(details)

    def Manage_Content(self):
        self.Create_Payment_Structure()
        self.context['date_from'] = self.request.session['root_users_payments_date_from']
        self.context['date_to'] = self.request.session['root_users_payments_date_to']
        self.context['button_address_name'] = 'root_address'
        return self.Render_HTML('root/users_payments.html')

    def Manage_Button(self):

        if self.request.POST['_name_'] == 'assign':
            index = self.Get_Post_Other('index')
            payment = SQL.Get(Model_Payment, pk=index)
            payment.status = self.request.POST['value']
            SQL.Save(data=payment)

        if self.request.POST['_name_'] == 'change':
            self.request.session['root_payment_status'] = \
                self.request.POST['value']

        return HttpResponse()

    def Manage_Filter(self):

        if self.request.POST['_name_'] == 'date_to':
            self.request.session['root_users_payments_date_to'] = \
                self.request.POST['value']

        if self.request.POST['_name_'] == 'date_from':
            self.request.session['root_users_payments_date_from'] = \
                self.request.POST['value']

        self.Validate_Period('root_users_payments_date_from', 'root_users_payments_date_to')
        return HttpResponse()

    def Manage_Form_Note(self):

        note = self.request.session['root_note']
        self.context['form'] = Form_Order_Note(self, post=True)

        if self.context['form'].is_valid():
            data = self.context['form'].cleaned_data
            note.note = data['note']
            SQL.Save(data=note)

            # save send files
            file = data['file']
            file_name = data['file_name']

            if file: # save if file was sent

                note_file = Model_Note_File()
                note_file.note = note
                note_file.name = file_name
                SQL.Save(data=note_file)

                note_file.Save_File(file)

            return Dialog_Prompt(self, apply=True).HTML
        return Dialog_Prompt(self, not_valid=True).HTML

    def Manage_Form_Deadline(self):

        dealdine = self.request.session['root_deadline']
        self.context['form'] = Form_Order_Deadline(
            self, post=True, instance=dealdine)

        if self.context['form'].is_valid():
            SQL.Save(data=self.context['form'])

            return Dialog_Prompt(self, apply=True).HTML
        return Dialog_Prompt(self, not_valid=True).HTML

    def Manage_Form_Send_Email(self):

        self.context['form'] = Form_Send_Email(self, post=True)
        if self.context['form'].is_valid():

            payment = self.request.session['root_payment']
            title = self.request.POST['title']
            message = self.request.POST['message']
            recipient = payment.user.email

            self.context['payment'] = payment
            self.context['message'] = message

            sender = Sender(self)
            sender.Send_Root_Email(title, self.context, recipient)
            return Dialog_Prompt(self, apply=True).HTML
        return Dialog_Prompt(self, not_valid=True).HTML

    def Manage_Form_Payment_Address(self):
        address = self.request.session['root_edit_payment_address']

        if address.__class__ == Model_Delivery_Address:
            self.context['form'] = Form_Delivery_Address(
                self, post=True, instance=address)

        if address.__class__ == Model_Invoice_Address:
            self.context['form'] = Form_Invoice_Address(
                self, post=True, instance=address)

        if self.context['form'].is_valid():
            self.context['form'].save()

            post = self.request.POST.copy()
            post.update(
                {
                    '_name_': 'root_address',
                    'value': address.payment.pk
                }
            )

            self.request.POST = post

            return Dialog_Alert(self).HTML
        return Dialog_Prompt(self, not_valid=True).HTML

    def Manage_Form(self):

        if self.request.POST['_name_'] == 'note':
            return self.Manage_Form_Note()

        if self.request.POST['_name_'] == 'deadline':
            return self.Manage_Form_Deadline()

        if self.request.POST['_name_'] == 'send_email':
            return self.Manage_Form_Send_Email()

        if self.request.POST['_name_'] == 'address_payment':
            return self.Manage_Form_Payment_Address()

        return Website_Manager.Manage_Form(self)

    @staticmethod
    def Launch(request):
        return Users_Payments(request, only_root=True).HTML
