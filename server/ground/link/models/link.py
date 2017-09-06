from server.ground.product.models import *
from server.ground.catalog.models import *


class Abstract_Model_Link(Abstract_Model):

    parent = models.ForeignKey(Model_Catalog, null=True)
    language = models.CharField(max_length=2)

    class Meta:
        abstract = True



class Model_Product_Link(Abstract_Model_Link):

    product = models.ForeignKey(Model_Product)

    def __str__(self):
        return self.product.name

    class Meta:
        unique_together = ('product', 'parent', 'language')



class Model_Catalog_Link(Abstract_Model_Link):

    catalog = models.ForeignKey(Model_Catalog, related_name='catalog')

    def __str__(self):
        return self.catalog.name

    class Meta:
        unique_together = ('catalog', 'parent', 'language')
