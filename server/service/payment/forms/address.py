from server.manage.switch.forms.address import *
from server.manage.switch.website import *


class Form_Delivery_Address(Abstract_Address_Form):

    class Meta(Abstract_Address_Form.Meta):
        model = Model_Delivery_Address
        exclude = ('user', 'payment',)



class Form_Invoice_Address(Abstract_Address_Form):

    class Meta(Abstract_Address_Form.Meta):
        model = Model_Invoice_Address
        exclude = ('user', 'payment',)
