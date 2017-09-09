from server.manage.switch.models.standard import *


class Model_Catalog(Abstract_Model):

    url_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    image = models.ImageField(blank=True)
    parent = models.ForeignKey('Model_Catalog', null=True)
    language = models.CharField(max_length=2, default=None)

    def Set_Variables(self):
        self.image_dir = 'img/catalog/'

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'parent', 'language')
