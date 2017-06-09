from server.arbuz.templatetags.base import *


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
        return name == 'ClearableFileInput'



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
