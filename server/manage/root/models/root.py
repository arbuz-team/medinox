from server.manage.switch.models import *


class Model_Root(Abstract_Model):

    password = models.CharField(max_length=75)

    def __str__(self):
        return 'Model_Root'



class Model_Root_Address(Abstract_Address):

    phone_1 = models.CharField(max_length=25)
    phone_2 = models.CharField(max_length=25)
    fax = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)



class Model_Social_Media(Abstract_Model):

    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    url = models.URLField()

    def __str__(self):
        return self.name



class Model_Delivery(Abstract_Model):

    price_on_receipt = models.FloatField()
    price_in_advance = models.FloatField()

