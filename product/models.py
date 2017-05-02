from arbuz.models import *
from user.models import User


class Brand(Abstract_Model):

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name



class Widget(Abstract_Model):

    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.name



class Values(Abstract_Model):

    name = models.CharField(max_length=50)
    super_price = models.IntegerField(default=0)
    widget = models.ForeignKey(Widget)

    def __str__(self):
        return self.name



class Catalog(Abstract_Model):

    url_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    image = models.ImageField(blank=True)
    parent = models.ForeignKey('Catalog', null=True)

    def Set_Variables(self):
        self.image_dir = '/_static/img/catalog/'

    def __str__(self):
        return self.name



class Product(Abstract_Model):

    url_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.IntegerField(blank=True)
    image = models.ImageField(blank=True)
    brand = models.ForeignKey(Brand, null=True, on_delete=models.SET_NULL)
    parent = models.ForeignKey(Catalog)

    def Set_Variables(self):
        self.image_dir = '/_static/img/product/'

    def __str__(self):
        return self.name



class Subproduct(Abstract_Model):

    unique = models.CharField(max_length=20)
    produkt = models.ForeignKey(Product)
    values = models.ManyToManyField(Values)

    def __str__(self):
        return self.unique



class Recommended_Product(Abstract_Model):

    product = models.ForeignKey(Product)

    def __str__(self):
        return self.product.details_en.name



class Favorite_Product(Abstract_Model):

    product = models.ForeignKey(Product)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.product.details_en.name
