from django.utils.safestring import mark_safe
from server.manage.switch.templatetags.base import *


# Backend: refactoring tags
class Product_Manager(Base_Tag_Manager):

    @staticmethod
    def Convert_Text_To_URL(text):
        text = text.replace(' ', '_').lower()
        return Dynamic_Base.Convert_Polish_To_Ascii(text)
