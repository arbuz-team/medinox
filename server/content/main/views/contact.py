from server.service.sender.views import *
from server.content.main.forms import *


class Contact(Website_Manager):

    def Create_Titles(self):

        self.content['form_detail'] = [
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

    def Manage_Content_Ground(self):
        language = self.request.session['translator_language']
        self.content['form'] = Form_Email_Contact(self)
        self.content['content'] = SQL.Filter(Contact_Content,
            language=language).order_by('position')

        self.Create_Titles()
        return self.Render_HTML('main/contact.html', 'email_contact')

    def Manage_Form(self):

        self.Create_Titles()
        self.content['form'] = Form_Email_Contact(self, post=True)

        if self.content['form'].is_valid():

            title = self.content['form'].cleaned_data['title']
            email = self.content['form'].cleaned_data['email']

            content = {
                'client':   self.content['form'].cleaned_data['client'],
                'question': self.content['form'].cleaned_data['message'],
                'product':  self.content['form'].cleaned_data['product'],
                'url':      self.content['form'].cleaned_data['url'],
            }

            Sender(self.request).Send_Contact_Question(title, content, email)

            return self.Render_HTML('main/contact.html', 'email_contact')
        return self.Render_HTML('main/contact.html', 'email_contact')

    @staticmethod
    def Launch(request):
        return Contact(request).HTML
