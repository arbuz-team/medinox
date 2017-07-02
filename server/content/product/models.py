from server.manage.user.models import User
from server.content.catalog.models import *


class Brand(Abstract_Model):

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name



class Product(Abstract_Model):

    url_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.IntegerField(blank=True)
    image = models.ImageField(blank=True)
    brand = models.ForeignKey(Brand, null=True, on_delete=models.SET_NULL)
    parent = models.ForeignKey(Catalog, null=True, on_delete=models.SET_NULL)
    # TODO language as one column

    def Set_Variables(self):
        self.image_dir = 'img/product/'

    def __str__(self):
        return self.name



class Description(Abstract_Model):

    header = models.CharField(max_length=200)
    paragraph = models.TextField()
    image = models.ImageField()
    product = models.ForeignKey(Product)

    def Set_Variables(self):
        self.image_dir = '/client/static/img/product/description/'

    def __str__(self):
        return self.header



class Widget(Abstract_Model):

    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    product = models.ForeignKey(Product)

    def __str__(self):
        return self.name



class Values(Abstract_Model):

    name = models.CharField(max_length=50)
    super_price = models.IntegerField(default=0)
    widget = models.ForeignKey(Widget)

    def __str__(self):
        return self.name



class Recommended_Product(Abstract_Model):

    product = models.ForeignKey(Product)

    def __str__(self):
        return self.product.details_en.name



class Favorite_Product(Abstract_Model):

    product = models.ForeignKey(Product)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.product.details_en.name
