from server.manage.switch.models import *


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

    currency = models.CharField(max_length=3)
    price = models.FloatField()

    @staticmethod
    def Get_Price(_object):
        currency = _object.request.session['currency_selected']
        return SQL.Get(Delivery, currency=currency).price
