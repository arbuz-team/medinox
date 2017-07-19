from server.dialog.service.base import *


class Service_Delete_Brand(Base_Service):

    def Manage(self):

        pk = self.request.POST['additional_value']
        brand = SQL.Get(Brand, pk=pk)
        products = SQL.Filter(Product, brand=brand)

        description = Text(self, 110)
        self.context['text'] = description.format(len(products))
        self.context['title'] = Text(self, 109)

        return self.Render_Dialog('confirm.html', only_root=True)
