from arbuz.views import *
from searcher.views import Search_Engine
from product.forms import *


class Start_App(Dynamic_Event_Manager):

    def Manage_Content_Ground(self):
        return self.Render_HTML('product/start.html')

    @staticmethod
    def Launch(request):
        return Start_App(request).HTML



class Details(Dynamic_Event_Manager):

    def Manage_Content_Ground(self):
        self.content['product'] = Product.objects.get(pk=self.other_value)
        widgets = Widget.objects.filter(product=self.content['product'])

        self.content['widgets'] = [
            {
                'widget': widget,
                'values': Values.objects.filter(widget=widget)
            }
            for widget in widgets
        ]

        self.request.session['product_last_selected'] = self.content['product']
        return self.Render_HTML('product/details.html')

    @staticmethod
    def Details(request, pk):
        return Details(request, other_value=pk).HTML

    @staticmethod
    def Launch(request):
        pass



class Add_Widget(Dynamic_Event_Manager):

    def Manage_Form_Widget(self):

        self.content['form'] = Form_Widget(
            self.request, self.request.POST)

        if self.content['form'].is_valid():
            widget = self.request.session['product_editing_widget']
            widget.name = self.content['form'].cleaned_data['name']
            widget.type = self.content['form'].cleaned_data['type']
            widget.save()

            return Dialog_Prompt(self.request, self.app_name, apply=True).HTML
        return Dialog_Prompt(self.request, self.app_name, not_valid=True).HTML

    # def Manage_Form_

    def Manage_Form(self):

        if 'widget' in self.request.POST['__form__']:
            return self.Manage_Form_Widget()

    @staticmethod
    def Launch(request):
        return Add_Widget(request).HTML
