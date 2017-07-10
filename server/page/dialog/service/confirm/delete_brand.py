from server.page.dialog.service.base import *


class Service_Delete_Brand(Base_Service):

    def Manage(self):

        pk = self.request.POST['additional_value']
        brand = SQL.Get(Brand, pk=pk)
        products = SQL.Filter(Product, brand=brand)

        description = Text(self, 110)
        self.content['text'] = description.format(len(products))
        self.content['title'] = Text(self, 109)

        return self.Render_Dialog('confirm.html', only_root=True)
