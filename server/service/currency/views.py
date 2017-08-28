from server.manage.switch.website import *


class Currency_Manager(Website_Manager):

    def Manage_Button(self):

        selected_currency = self.request.POST['value']
        if selected_currency in ['PLN', 'EUR', 'GBP']:
            self.request.session['language_currency'] = \
                selected_currency

        return HttpResponse()

    @staticmethod
    def Launch(request):
        return Currency_Manager(request).HTML
