from server.manage.switch.forms.media import *


class Form_PayPal(Abstract_Form):

    def Create_Fields(self):

        # payment details
        self.fields['business'] = forms.CharField(widget=forms.HiddenInput())
        self.fields['amount'] = forms.CharField(widget=forms.HiddenInput())
        self.fields['currency_code'] = forms.CharField(widget=forms.HiddenInput())
        self.fields['item_name'] = forms.CharField(widget=forms.HiddenInput())

        # user details
        self.fields['custom'] = forms.CharField(widget=forms.HiddenInput())

        # service details
        self.fields['cmd'] = forms.CharField(widget=forms.HiddenInput(), initial='_xclick')
        self.fields['charset'] = forms.CharField(widget=forms.HiddenInput(), initial='utf-8')
        self.fields['no_shipping'] = forms.CharField(widget=forms.HiddenInput(), initial='1')

        # URLS
        self.fields['notify_url'] = forms.CharField(widget=forms.HiddenInput())
        self.fields['cancel_return'] = forms.CharField(widget=forms.HiddenInput())
        self.fields['return'] = forms.CharField(widget=forms.HiddenInput())



# PayU
# http://developers.payu.com/pl/restapi.html#references_form_pimage_urlarameters



# przelewy24
# Page: 5/15
# https://www.przelewy24.pl/storage/app/media/pobierz/Instalacja/przelewy24_specyfikacja_3_2.pdf

