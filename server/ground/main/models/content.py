from server.manage.switch.models import *


class Model_Content_Tab(Abstract_Model):

    header = models.CharField(max_length=200)
    paragraph = models.TextField()
    image = models.ImageField()
    language = models.CharField(max_length=2)

    class Meta:
        abstract = True

    def __str__(self):
        return self.header



class Model_About_Content(Model_Content_Tab):

    def Set_Variables(self):
        self.image_dir = 'img/about/'



class Model_Contact_Content(Model_Content_Tab):

    def Set_Variables(self):
        self.image_dir = 'img/contact/'
