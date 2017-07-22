from server.manage.switch.website.manager import *
from server.service.payment.forms import *


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
        payments = SQL.Filter(Payment, status=status,
                      date__gte=date_from, date__lte=date_to)

        for payment in payments:

            details = {
                'fullname': SQL.Get(Invoice_Address, payment=payment).full_name,
                'payment':  payment,
                'products': SQL.Filter(Selected_Product, payment=payment)
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
            payment = SQL.Get(Payment, pk=index)
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
        form_note = Form_Order_Note(self, post=True)

        if form_note.is_valid():
            note.note = form_note.cleaned_data['note']
            SQL.Save(data=note)

            # save send files
            file = form_note.cleaned_data['file']
            file_name = form_note.cleaned_data['file_name']

            if file: # save if file was sent

                note_file = Note_File()
                note_file.note = note
                note_file.name = file_name
                SQL.Save(data=note_file)

                note_file.Save_File(file)

            return Dialog_Prompt(self, apply=True).HTML
        return Dialog_Prompt(self, not_valid=True).HTML

    def Manage_Form_Deadline(self):

        note = self.request.session['root_deadline']
        form_deadline = Form_Order_Deadline(
            self, post=True, instance=note)

        if form_deadline.is_valid():
            SQL.Save(data=form_deadline)

            return Dialog_Prompt(self, apply=True).HTML
        return Dialog_Prompt(self, not_valid=True).HTML

    def Manage_Form(self):

        if self.request.POST['_name_'] == 'note':
            return self.Manage_Form_Note()

        if self.request.POST['_name_'] == 'deadline':
            return self.Manage_Form_Deadline()

        return Website_Manager.Manage_Form(self)

    @staticmethod
    def Launch(request):
        return Users_Payments(request, only_root=True).HTML
