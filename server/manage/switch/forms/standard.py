from server.manage.switch.forms.base import *


class Abstract_Model_Form(Base_Form, forms.ModelForm):

    def Edit_Instance(self):
        pass

    def Exclude_Fields(self):

        keys = ['position', 'deleted']

        for key in keys:
            if key in self.fields:
                del self.fields[key]

    def __init__(self, _object, post=False, *args, **kwargs):

        if 'instance' in kwargs:
            self.instance = kwargs['instance']
            self.Edit_Instance()

        if post: forms.ModelForm.__init__(self,
              _object.request.POST, *args, **kwargs)

        else: forms.ModelForm.__init__(self, *args, **kwargs)
        Base_Form.__init__(self, _object)



class Abstract_Form(Base_Form, forms.Form):

    def __init__(self, _object, post=False, *args, **kwargs):

        if post: forms.Form.__init__(self,
             _object.request.POST, *args, **kwargs)

        else: forms.Form.__init__(self, *args, **kwargs)
        Base_Form.__init__(self, _object)
