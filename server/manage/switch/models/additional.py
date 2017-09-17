from server.manage.switch.models.standard import *
from django_countries.fields import CountryField


class Abstract_Address(Abstract_Model):

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    nip = models.CharField(max_length=20)
    address_line = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    region = models.CharField(max_length=50)  # state/province/region
    postcode = models.CharField(max_length=10)  # zip/postal code
    country = CountryField()

    class Meta:
        abstract = True

    def __str__(self):
        return '{0} {1}'.format(self.name, self.surname)


