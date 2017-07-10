from server.manage.switch.models.standard import *


class Root(Abstract_Model):

    password = models.CharField(max_length=75)

    def __str__(self):
        return 'Root'



class Root_Address(Abstract_Address):

    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)



class Social_Media(Abstract_Model):

    name = models.CharField(max_length=20)
    url = models.URLField()

    def __str__(self):
        return self.name



class Delivery(Abstract_Model):

    country = models.CharField(max_length=20)
    price_eur = models.IntegerField()
    price_pln = models.IntegerField()
