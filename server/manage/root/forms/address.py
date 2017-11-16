from server.manage.switch.forms.address import *
from server.manage.root.models import *


class Form_Root_Address(Abstract_Address_Form):

    def Create_Fields(self):
        for key in self.fields:
            self.fields[key].required = False

    def Set_Widgets(self):

        phone_1_attr = self.Attr(Text(self, 139))
        phone_2_attr = self.Attr(Text(self, 139))
        fax_attr = self.Attr(Text(self, 198))
        email_attr = self.Attr(Text(self, 140), classes='test')

        self.fields['phone_1'].widget = forms.TextInput(attrs=phone_1_attr)
        self.fields['phone_2'].widget = forms.TextInput(attrs=phone_2_attr)
        self.fields['fax'].widget = forms.TextInput(attrs=fax_attr)
        self.fields['email'].widget = forms.TextInput(attrs=email_attr)

        Abstract_Address_Form.Set_Widgets(self)

    class Meta(Abstract_Address_Form.Meta):
        model = Model_Root_Address



class Form_Shop_Address(Abstract_Address_Form):

    def Exclude_Fields(self):
        del self.fields['nip']

    def Create_Fields(self):
        for key in self.fields:
            self.fields[key].required = False

    def Set_Widgets(self):

        phone_1_attr = self.Attr(Text(self, 139))
        phone_2_attr = self.Attr(Text(self, 139))
        fax_attr = self.Attr(Text(self, 198))
        email_attr = self.Attr(Text(self, 140), classes='test')

        self.fields['phone_1'].widget = forms.TextInput(attrs=phone_1_attr)
        self.fields['phone_2'].widget = forms.TextInput(attrs=phone_2_attr)
        self.fields['fax'].widget = forms.TextInput(attrs=fax_attr)
        self.fields['email'].widget = forms.TextInput(attrs=email_attr)

        Abstract_Address_Form.Set_Widgets(self)

    class Meta(Abstract_Address_Form.Meta):
        model = Model_Root_Address