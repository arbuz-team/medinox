from markdownx.fields import MarkdownxFormField
from server.manage.switch.forms.address import *
from server.manage.switch.website import *


class Form_User_Address(Abstract_Address_Form):

    class Meta(Abstract_Address_Form.Meta):
        model = Model_User_Address
        exclude = ('user', )



class Form_Markdown(forms.Form):

    markdown = MarkdownxFormField()