from arbuz.models import *
from user.models import User


class Details(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Details_EN(Details):
    pass

class Details_PL(Details):
    pass

class Details_DE(Details):
    pass



class Where_Display(models.Model):

    display_en = models.BooleanField()
    display_pl = models.BooleanField()
    display_de = models.BooleanField()

    def __str__(self):
        return 'en: {0}, pl: {1}, de: {2}'\
            .format(self.display_en, self.display_pl, self.display_de)



class Brand(models.Model):

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name



class Purpose(models.Model):

    name_en = models.CharField(max_length=20)
    name_pl = models.CharField(max_length=20)
    name_de = models.CharField(max_length=20)

    def __str__(self):
        return self.name_en



class Product(Abstract_Model):

    details_en = models.ForeignKey(Details_EN, null=True)
    details_pl = models.ForeignKey(Details_PL, null=True)
    details_de = models.ForeignKey(Details_DE, null=True)

    price_eur = models.IntegerField(blank=True)
    price_pln = models.IntegerField(blank=True)

    image = models.ImageField(blank=True)
    keywords = models.TextField(blank=True)
    stock = models.IntegerField(blank=True)

    where_display = models.ForeignKey(Where_Display)
    brand = models.ForeignKey(Brand, null=True, on_delete=models.SET_NULL)
    purpose = models.ManyToManyField(Purpose)

    def Set_Variables(self):
        self.image_dir = '/_static/img/product/'

    def __str__(self):
        return self.details_en.name



class Recommended_Product(models.Model):

    product = models.ForeignKey(Product)

    def __str__(self):
        return self.product.details_en.name



class Favorite_Product(models.Model):

    product = models.ForeignKey(Product)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.product.details_en.name
