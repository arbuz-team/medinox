from server.manage.switch.models import *
from server.ground.product.models import *
from server.manage.root.models import Delivery


class Payment(Abstract_Model):

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



class Selected_Product(Abstract_Model):

    payment = models.ForeignKey(Payment)
    product = models.ForeignKey(Product)
    values = models.ManyToManyField(Values)
    number = models.IntegerField()

    def __str__(self):
        return self.product.name



class Order_Deadline(Abstract_Model):

    payment = models.OneToOneField(Payment)
    name = models.CharField(max_length=20)
    deadline = models.DateField(null=True)
    send_to_buyer = models.BooleanField()
    send_to_root = models.BooleanField()
    reminder = models.DateField(null=True)



class Order_Note(Abstract_Model):

    payment = models.OneToOneField(Payment)
    note = models.TextField()



class Note_File(Abstract_Model):

    name = models.CharField(max_length=50)
    file = models.FileField()
    note = models.ForeignKey(Order_Note)

    def Set_Variables(self):
        self.file_dir = 'files/orders/'