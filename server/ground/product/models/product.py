from server.manage.user.models import Model_User
from server.ground.catalog.models import *
from server.manage.switch.models import *


class Model_Brand(Abstract_Model):

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name



class Model_Prices(Abstract_Model):

    eur = models.FloatField()
    pln = models.FloatField()
    gbp = models.FloatField()

    def __str__(self):
        return '{0} eur, {1} pln, {2} gbp'\
            .format(self.eur, self.pln, self.gbp)

    def Get_Price(self, _object):

        switch = {
            'EUR': self.eur,
            'PLN': self.pln,
            'GBP': self.gbp
        }

        currency = _object.request.session['currency_selected']
        return switch[currency]



class Model_Product(Abstract_Model):

    url_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    image = models.ImageField(blank=True)
    price = models.ForeignKey(Model_Prices, null=True, on_delete=models.SET_NULL)
    brand = models.ForeignKey(Model_Brand, null=True, on_delete=models.SET_NULL)
    parent = models.ForeignKey(Model_Catalog, null=True, on_delete=models.SET_NULL)
    language = models.CharField(max_length=2)

    def Set_Variables(self):
        self.image_dir = 'img/product/'

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'parent', 'language')



class Model_Description(Abstract_Model):

    header = models.CharField(max_length=200)
    paragraph = models.TextField()
    image = models.ImageField()
    product = models.ForeignKey(Model_Product)

    def Set_Variables(self):
        self.image_dir = 'img/product/description/'

    def __str__(self):
        return self.header



class Model_Widget(Abstract_Model):

    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    product = models.ForeignKey(Model_Product)

    def __str__(self):
        return self.name



class Model_Values(Abstract_Model):

    name = models.CharField(max_length=50)
    super_price = models.IntegerField(default=0)
    widget = models.ForeignKey(Model_Widget)

    def __str__(self):
        return self.name



class Model_Recommended_Product(Abstract_Model):

    product = models.OneToOneField(Model_Product)

    def __str__(self):
        return self.product.details_en.name



class Model_Favorite_Product(Abstract_Model):

    product = models.ForeignKey(Model_Product)
    user = models.ForeignKey(Model_User)

    class Meta:
        unique_together = ('product', 'user')

    def __str__(self):
        return self.product.details_en.name
