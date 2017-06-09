from server.product.models import *
from server.root.models import Delivery


class Payment(models.Model):

    user = models.ForeignKey(User)
    date = models.DateField()
    total_price = models.CharField(max_length=10)
    delivery_price = models.ForeignKey(Delivery)
    currency = models.CharField(max_length=3)
    service = models.CharField(max_length=10)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username



class Delivery_Address(Abstract_Address):
    payment = models.OneToOneField(Payment)



class Invoice_Address(Abstract_Address):
    payment = models.OneToOneField(Payment)



class Selected_Product(models.Model):

    payment = models.ForeignKey(Payment)
    product = models.ForeignKey(Product)
    values = models.ManyToManyField(Values)
    number = models.IntegerField()

    def __str__(self):
        return self.product.name
