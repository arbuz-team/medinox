from product.forms import *
from user.account.forms import *
from main.forms import *
from payment.models import *
from main.models import *
from translator.views import *
from inspect import getmembers, ismethod


class Dialog(Dynamic_Base):

    def Get_POST_Variable(self, name):

        if name in self.request.POST:
            return self.request.POST[name]

        else: return ''

    def Generate_Content(self):

        self.content['additional'] = {
            'name':     self.Get_POST_Variable('additional_name'),
            'action':   self.Get_POST_Variable('additional_action'),
            'value':    self.Get_POST_Variable('additional_value'),
            'reload':   self.Get_POST_Variable('additional_reload'),
            'redirect': self.Get_POST_Variable('additional_redirect'),
            'url':      self.Get_POST_Variable('additional_url'),
            'event':    self.Get_POST_Variable('additional_event'),
        }

    def Render_Dialog(self, file_name, form_name = '',
                      authorization=False, only_root=False):

        if not authorization and not only_root:
            return self.Render_HTML(file_name, form_name)

        if authorization:
            if self.request.session['user_login']:
                return self.Render_HTML(file_name, form_name)

        if only_root:
            if self.request.session['root_login']:
                return self.Render_HTML(file_name, form_name)

        return self.Unauthorized_Access()

    def Get_Dialog_Name(self):
        return self.request.POST['dialog_name']

    @staticmethod
    def Apply_Message():
        return JsonResponse({'__form__': 'true'})

    def Unauthorized_Access(self):
        self.content['title'] = Text(self.request, 69)
        self.content['text'] = Text(self.request, 70)
        return self.Render_HTML('dialog/alert.html')

    def Manage(self):

        if self.apply:
            return self.Apply_Message()

        # content for buttons in dialogs
        self.Generate_Content()

        methods = getmembers(self, predicate=ismethod)
        methods = [method[0] for method in methods]
        dialog_name = self.Get_Dialog_Name()

        for method in methods:
            if dialog_name in method.lower():
                return getattr(self.__class__, method)(self)

    def __init__(self, request, app_name, apply=False):
        Dynamic_Base.__init__(self, request)
        self.parent_app_name= app_name
        self.apply = apply



class Dialog_Alert(Dialog):

    def Manage_Language(self):
        return self.Render_Dialog('dialog/language.html')

    def Manage_Product_Recommended(self):
        self.content['title'] = Text(self.request, 9)
        self.content['text'] = Text(self.request, 10)
        return self.Render_Dialog('dialog/alert.html', only_root=True)

    def Manage_Root_Address(self):
        payment = Payment.objects.get(pk=self.request.POST['dialog_value'])
        self.content['invoice'] = Invoice_Address.objects.get(payment=payment)
        self.content['delivery'] = Delivery_Address.objects.get(payment=payment)
        return self.Render_Dialog('dialog/address.html', only_root=True)

    def Manage_User_Address(self):
        payment = Payment.objects.get(pk=self.request.POST['dialog_value'])
        self.content['invoice'] = Invoice_Address.objects.get(payment=payment)
        self.content['delivery'] = Delivery_Address.objects.get(payment=payment)
        return self.Render_Dialog('dialog/address.html', authorization=True)

    def Manage_Icons(self):
        self.content['title'] = Text(self.request, 137)
        self.content['text'] = Text(self.request, 138)
        return self.Render_Dialog('dialog/alert.html')

    def __init__(self, request, app_name):
        Dialog.__init__(self, request, app_name)
        self.HTML = self.Manage()



class Dialog_Confirm(Dialog):

    def Manage_Delete_Product(self):
        self.content['title'] = Text(self.request, 98)
        self.content['text'] = Text(self.request, 99)
        return self.Render_Dialog('dialog/confirm.html', only_root=True)

    def Manage_Delete_Address(self):
        self.content['title'] = Text(self.request, 107)
        self.content['text'] = Text(self.request, 108)
        return self.Render_Dialog('dialog/confirm.html', authorization=True)

    def Manage_Delete_Brand(self):
        self.content['title'] = Text(self.request, 109)
        description = Text(self.request, 110)

        brand = Brand.objects.get(pk=self.request.POST['additional_value'])
        products = Product.objects.filter(brand=brand)
        self.content['text'] = description.format(len(products))

        return self.Render_Dialog('dialog/confirm.html', only_root=True)

    def Manage_Delete_About(self):
        self.content['title'] = Text(self.request, 153)
        self.content['text'] = Text(self.request, 154)
        return self.Render_Dialog('dialog/confirm.html', only_root=True)

    def Manage_Delete_Purpose(self):
        self.content['title'] = Text(self.request, 111)
        description = Text(self.request, 112)

        purpose = Purpose.objects.get(pk=self.request.POST['additional_value'])
        products = Product.objects.filter(purpose=purpose)
        self.content['text'] = description.format(len(products))

        return self.Render_Dialog('dialog/confirm.html', only_root=True)

    def Manage_Clear_Cart(self):
        self.content['title'] = Text(self.request, 100)
        self.content['text'] = Text(self.request, 101)
        return self.Render_Dialog('dialog/confirm.html', authorization=True)

    def __init__(self, request, app_name):
        Dialog.__init__(self, request, app_name)
        self.HTML = self.Manage()



class Dialog_Prompt(Dialog):

    def Generate_Content(self):

        self.content['additional'] = {
            'reload': self.request.POST['additional_reload'],
            'redirect': self.request.POST['additional_redirect'],
            'event': self.request.POST['additional_event'],
        }


    def Manage_Brand(self):
        initial = self.Get_Session_Variable()
        self.content['title'] = Text(self.request, 1)
        self.content['form'] = Form_Brand(self.request,
            self.Get_POST(), initial={'brands': initial})

        return self.Render_Dialog('dialog/create_or_select.html',
                                  'brand', only_root=True)

    def Manage_Purpose(self):
        initial = self.Get_Session_Variable()
        self.content['title'] = Text(self.request, 2)
        self.content['form'] = Form_Purpose(self.request,
            self.Get_POST(), initial=initial)

        return self.Render_Dialog('dialog/create_or_select.html',
                                  'purpose', only_root=True)

    def Manage_Details_EN(self):
        self.content['title'] = Text(self.request, 3)
        self.content['form'] = Form_Details_EN(self.request,
            self.Get_POST(), instance=self.Get_Session_Variable())

        return self.Render_Dialog('dialog/prompt.html',
                                  'details_en', only_root=True)

    def Manage_Details_PL(self):
        self.content['title'] = Text(self.request, 4)
        self.content['form'] = Form_Details_PL(self.request,
            self.Get_POST(), instance=self.Get_Session_Variable())

        return self.Render_Dialog('dialog/prompt.html',
                                  'details_pl', only_root=True)

    def Manage_Details_DE(self):
        self.content['title'] = Text(self.request, 5)
        self.content['form'] = Form_Details_EN(self.request,
            self.Get_POST(), instance=self.Get_Session_Variable())

        return self.Render_Dialog('dialog/prompt.html',
                                  'details_de', only_root=True)

    def Manage_Where_Display(self):
        self.content['title'] = Text(self.request, 6)
        self.content['form'] = Form_Where_Display(self.request,
            self.Get_POST(), instance=self.Get_Session_Variable())

        return self.Render_Dialog('dialog/prompt.html',
                                  'where_display', only_root=True)

    def Manage_Image(self):
        initial = self.Get_Session_Variable()
        url = self.request.session['product_image_url']

        self.content['title'] = Text(self.request, 7)
        self.content['image'] = initial
        self.content['form'] = Form_Image(self.request,
            self.Get_POST(), initial={'url': url})

        return self.Render_Dialog('dialog/prompt.html',
                                  'image', only_root=True)


    def Manage_Edit_Email(self):
        self.content['title'] = Text(self.request, 86)
        self.content['form'] = Form_User_Details(
            self.request, self.Get_POST())

        self.content['form'].Set_Hidden('new_username')
        self.content['form'].Set_Hidden('new_password')

        return self.Render_Dialog('dialog/prompt.html',
                                  'edit_email', authorization=True)

    def Manage_Edit_Username(self):
        self.content['title'] = Text(self.request, 87)
        self.content['form'] = Form_User_Details(
            self.request, self.Get_POST())

        self.content['form'].Set_Hidden('new_email')
        self.content['form'].Set_Hidden('new_password')

        return self.Render_Dialog('dialog/prompt.html',
                                  'edit_username', authorization=True)

    def Manage_Edit_Password(self):
        self.content['title'] = Text(self.request, 88)
        self.content['form'] = Form_User_Details(
            self.request, self.Get_POST())

        self.content['form'].Set_Hidden('new_username')
        self.content['form'].Set_Hidden('new_email')

        return self.Render_Dialog('dialog/prompt.html',
                                  'edit_password', authorization=True)


    def Manage_Edit_Content_Tab(self):

        pk = self.request.POST['dialog_value']
        content = Content_Tab.objects.get(pk=pk)
        initial = {
            'header':       content.header,
            'paragraph':    content.paragraph,
        }

        self.request.session['main_content_tab'] = content
        self.content['title'] = Text(self.request, 93)
        self.content['image'] = content.image
        self.content['form'] = Form_Content_Tab(self.request,
            self.Get_POST(), initial=initial)

        return self.Render_Dialog('dialog/prompt.html',
                                  'content_tab', only_root=True)


    def Get_POST(self):

        if self.not_valid:
            return self.request.POST

        return None

    def Get_Session_Variable(self):

        session_variable = '{0}_{1}'.format(
            self.parent_app_name, self.Get_Dialog_Name())

        if session_variable in self.request.session:
            if self.request.session[session_variable]:
                return self.request.session[session_variable]

        return None

    def Get_Dialog_Name(self):

        if '__form__' in self.request.POST:
            return self.request.POST['__form__']

        return self.request.POST['dialog_name']

    def __init__(self, request, app_name, apply=False, not_valid=False):
        Dialog.__init__(self, request, app_name, apply)
        self.not_valid = not_valid
        self.HTML = self.Manage()
