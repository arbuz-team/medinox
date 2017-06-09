from server.manage.switch.models import *


class Catalog(Abstract_Model):

    url_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    image = models.ImageField(blank=True)
    parent = models.ForeignKey('Catalog', null=True)

    def Set_Variables(self):
        self.image_dir = '/static/img/catalog/'

    def __str__(self):
        return self.name
