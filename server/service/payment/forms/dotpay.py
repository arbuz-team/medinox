from server.manage.switch.forms.media import *


class Form_Dotpay(Abstract_Form):

    def Create_Fields(self):

        # payment details
        self.fields['id'] = forms.CharField(widget=forms.HiddenInput())
        self.fields['amount'] = forms.CharField(widget=forms.HiddenInput())
        self.fields['currency'] = forms.CharField(widget=forms.HiddenInput())
        self.fields['description'] = forms.CharField(widget=forms.HiddenInput())

        # user details
        self.fields['control'] = forms.CharField(widget=forms.HiddenInput())
        self.fields['firstname'] = forms.CharField(widget=forms.HiddenInput())
        self.fields['lastname'] = forms.CharField(widget=forms.HiddenInput())
        self.fields['email'] = forms.CharField(widget=forms.HiddenInput())

        # service details
        self.fields['ch_lock'] = forms.CharField(widget=forms.HiddenInput(), initial='0')
        self.fields['channel'] = forms.CharField(widget=forms.HiddenInput(), initial='0')
        self.fields['type'] = forms.CharField(widget=forms.HiddenInput(), initial='3')
        self.fields['lang'] = forms.CharField(widget=forms.HiddenInput())

        # URLS
        self.fields['URL'] = forms.CharField(widget=forms.HiddenInput())
        self.fields['URLC'] = forms.CharField(widget=forms.HiddenInput())

# Dotpay
# Page: 8/44
# https://ssl.dotpay.pl/s2/login/cloudfs1/magellan_media/common_file/dotpay_instrukcja_techniczna_implementacji_platnosci.pdf

