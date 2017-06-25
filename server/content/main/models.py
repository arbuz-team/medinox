from server.manage.switch.models import *


class Content_Tab(Abstract_Model):

    tab_name = models.CharField(max_length=20)
    header = models.CharField(max_length=200)
    paragraph = models.TextField()
    image = models.ImageField()
    language = models.CharField(max_length=2)

    def Set_Variables(self):
        self.image_dir = '/client/static/img/content_tab/'

    def __str__(self):
        return self.header
