from server.manage.switch.forms import *
from server.service.payment.models import *


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



class Form_Order_Deadline(Abstract_Model_Form):

    def Create_Fields(self):

        self.fields['name'] = forms.CharField()
        self.fields['deadline'] = forms.DateField(required=False)
        self.fields['reminder'] = forms.DateField(required=False)
        self.fields['send_to_buyer'] = forms.BooleanField(required=False)
        self.fields['send_to_root'] = forms.BooleanField(required=False)

    def Set_Widgets(self):

        name_attr = self.Attr(Text(self, 170))
        deadline_attr = self.Attr(other={'type': 'date'}, field=Field.DATE)
        reminder_attr = self.Attr(other={'type': 'date'}, field=Field.DATE)
        stb_attr = self.Attr(field=Field.CHECKBOX)
        str_attr = self.Attr(field=Field.CHECKBOX)

        self.fields['name'].widget = forms.TextInput(attrs=name_attr)
        self.fields['deadline'].widget = forms.DateInput(attrs=deadline_attr)
        self.fields['reminder'].widget = forms.DateInput(attrs=reminder_attr)
        self.fields['send_to_buyer'].widget = forms.CheckboxInput(attrs=stb_attr)
        self.fields['send_to_root'].widget = forms.CheckboxInput(attrs=str_attr)

    class Meta:
        model = Order_Deadline
        fields = ('name', 'deadline', 'reminder',
                  'send_to_buyer', 'send_to_root')



class Form_Order_Note(Abstract_File_Form):

    def Create_Fields(self):
        self.fields['note'] = forms.CharField(required=False)
        Abstract_File_Form.Create_Fields(self)

    def Set_Widgets(self):
        note_attr = self.Attr(Text(self, 169), field=Field.TEXTAREA)
        self.fields['note'].widget = forms.Textarea(attrs=note_attr)
        Abstract_File_Form.Set_Widgets(self)
