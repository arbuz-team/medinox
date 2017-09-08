from server.manage.switch.templatetags.base import *
from server.ground.link.models import *


class Check_Manager(Base_Tag_Manager):

    def If_Field_Is_Checkbox(self):
        field = self.values['field']
        name = field.field.widget.__class__.__name__
        return name == 'CheckboxInput'

    def If_Field_Is_Radio(self):
        field = self.values['field']
        name = field.field.widget.__class__.__name__
        return name == 'RadioSelect'

    def If_Field_Is_FileInput(self):
        field = self.values['field']
        name = field.field.widget.__class__.__name__
        return name == 'FileInput'



@register.filter
def is_checkbox(field):

    task = 'If_Field_Is_Checkbox'
    values = {'field': field}

    return Check_Manager(task, values).OUT

@register.filter
def is_radio(field):

    task = 'If_Field_Is_Radio'
    values = {'field': field}

    return Check_Manager(task, values).OUT

@register.filter
def is_fileinput(field):

    task = 'If_Field_Is_FileInput'
    values = {'field': field}

    return Check_Manager(task, values).OUT

@register.filter
def is_catalog(element):
    return element.__class__ == Model_Catalog

@register.filter
def is_product(element):
    return element.__class__ == Model_Product

@register.filter
def is_catalog_link(element):
    return element.__class__ == Model_Catalog_Link

@register.filter
def is_product_link(element):
    return element.__class__ == Model_Product_Link
