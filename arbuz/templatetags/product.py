from django.utils.safestring import mark_safe
from arbuz.templatetags.base import *


class Product_Manager(Base_Tag_Manager):

    @staticmethod
    def Convert_Text_To_URL(text):
        text = text.replace(' ', '_').lower()
        return Dynamic_Base.Convert_Polish_To_Ascii(text)

    def Get_Product_Name(self):
        product = self.values['product']
        name = Product_Models_Manager(self.request)\
            .Get_Product_Name(product)

        if 'to_url' in self.values:
            return self.Convert_Text_To_URL(name)

        return name

    def Get_Product_Description(self):
        product = self.values['product']
        description = Product_Models_Manager(self.request)\
            .Get_Product_Description(product)

        return mark_safe(description.replace('\n', '<br>'))

    def Get_Purpose_Name(self):
        purpose = self.values['purpose']
        name = Product_Models_Manager(self.request)\
            .Get_Purpose_Name(purpose)

        return name



@register.simple_tag(takes_context=True)
def product_name(context, product):

    task = 'Get_Product_Name'
    request = context['request']
    values = {'product': product}

    return Product_Manager(task, values, request).OUT

@register.simple_tag(takes_context=True)
def product_description(context, product):

    task = 'Get_Product_Description'
    request = context['request']
    values = {'product': product}

    return Product_Manager(task, values, request).OUT

@register.simple_tag(takes_context=True)
def product_name_url(context, product):

    task = 'Get_Product_Name'
    request = context['request']
    values = {
        'product': product,
        'to_url': True
    }

    return Product_Manager(task, values, request).OUT

@register.simple_tag(takes_context=True)
def purpose_name(context, purpose):

    task = 'Get_Purpose_Name'
    request = context['request']
    values = {'purpose': purpose}

    return Product_Manager(task, values, request).OUT
