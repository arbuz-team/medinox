from server.page.dialog.service.base import *


class Service_Delete_Brand(Base_Service):

    def Manage(self):

        pk = self.request.POST['additional_value']
        brand = Brand.objects.get(pk=pk)
        products = Product.objects.filter(brand=brand)

        description = Text(self.request, 110)
        self.content['text'] = description.format(len(products))
        self.content['title'] = Text(self.request, 109)

        return self.dialog.Render_Dialog(
            'dialog/confirm.html', only_root=True)
