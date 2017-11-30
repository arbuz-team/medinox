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



class Model_Shop_Address(Abstract_Address):

    phone_1 = models.CharField(max_length=25)
    phone_2 = models.CharField(max_length=25)
    fax = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)



class Model_Social_Media(Abstract_Model):

    name = models.IntegerField()
    type = models.CharField(max_length=20)
    url = models.URLField()

    def __str__(self):
        return self.name



class Model_Delivery(Abstract_Model):

    delivery_price = models.FloatField()
    cash_on_delivery = models.FloatField()



class Model_Delivery_Method(Abstract_Model):

    method = models.CharField(max_length=30)
    is_active = models.BooleanField()



class Model_Payment_Method(Abstract_Model):

    method = models.CharField(max_length=30)
    is_active = models.BooleanField()



class Model_Data_For_Public(Abstract_Model):

    names = models.BooleanField()
    phones = models.BooleanField()
    address = models.BooleanField()
    email = models.BooleanField()
    shop_address = models.BooleanField()

    def __str__(self):
        return str({'names': self.names, 'phones': self.phones,
                    'address': self.address, 'email': self.email,
                    'shop_address': self.shop_address})
