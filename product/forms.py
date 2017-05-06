from arbuz.forms import *
from product.models import *


class Form_Widget(Abstract_Model_Form):

    class Meta:

        model = Widget
        fields = (
            'name',
            'type',
        )
