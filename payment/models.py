from django.db import models
from user.models import User, Abstract_Address
from product.models import Product
from root.models import Delivery


class Payment(models.Model):

    user = models.ForeignKey(User)
    date = models.DateField()
    total_price = models.CharField(max_length=10)
    delivery_price = models.ForeignKey(Delivery)
    currency = models.CharField(max_length=3)
    service = models.CharField(max_length=10)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username



class Delivery_Address(Abstract_Address):
    payment = models.OneToOneField(Payment)



class Invoice_Address(Abstract_Address):
    payment = models.OneToOneField(Payment)



class Selected_Product(models.Model):

    payment = models.ForeignKey(Payment)
    product = models.ForeignKey(Product)
    number = models.IntegerField()

    def __str__(self):
        return self.product.details_en.name
