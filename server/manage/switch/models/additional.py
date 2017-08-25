from server.manage.switch.models.standard import *
from django_countries.fields import CountryField


class Abstract_Address(Abstract_Model):

    full_name = models.CharField(max_length=50)
    doctor_number = models.CharField(max_length=7) # for polish users
    address_line = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    region = models.CharField(max_length=50)  # state/province/region
    postcode = models.CharField(max_length=10)  # zip/postal code
    country = CountryField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.full_name


