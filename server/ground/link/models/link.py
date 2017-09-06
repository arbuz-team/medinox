from server.ground.product.models import *
from server.ground.catalog.models import *


class Model_Product_Link(Abstract_Model):

    product = models.ForeignKey(Model_Product)

    def __str__(self):
        return self.product.name



class Model_Catalog_Link(Abstract_Model):

    catalog = models.ForeignKey(Model_Catalog)

    def __str__(self):
        return self.catalog.name
