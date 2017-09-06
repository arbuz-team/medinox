from server.service.sender.views import *
from server.ground.main.forms import *


class Contact(Website_Manager):

    def Create_Titles(self):

        self.context['form_detail'] = [
            {
                'title':    Text(self, 81),
                'hidden':   'url',
            },
            {
                'title':    Text(self, 82),
                'hidden':   'product',
            },
            {
                'title':    Text(self, 83),
                'hidden':   'url product',
            },
        ]

    def Manage_Content(self):
        language = self.request.session['translator_language']
        self.context['form'] = Form_Email_Contact(self)
        self.context['content'] = SQL.Filter(Model_Contact_Content,
            language=language).order_by('position')

        self.Create_Titles()
        return self.Render_HTML('main/contact.html', 'email_contact')

    def Manage_Form(self):

        self.Create_Titles()
        self.context['form'] = Form_Email_Contact(self, post=True)

        if self.context['form'].is_valid():

            title = self.context['form'].cleaned_data['title']
            email = self.context['form'].cleaned_data['email']

            content = {
                'client':   self.context['form'].cleaned_data['client'],
                'question': self.context['form'].cleaned_data['message'],
                'product':  self.context['form'].cleaned_data['product'],
                'url':      self.context['form'].cleaned_data['url'],
            }

            Sender(self).Send_Contact_Question(title, content, email)

            return self.Render_HTML('main/contact.html', 'email_contact')
        return self.Render_HTML('main/contact.html', 'email_contact')

    @staticmethod
    def Launch(request):
        return Contact(request).HTML
