from server.manage.switch.models import *


class Language_EN(Abstract_Model):
    value = models.CharField(max_length=200)

class Language_PL(Abstract_Model):
    value = models.CharField(max_length=200)

class Language_DE(Abstract_Model):
    value = models.CharField(max_length=200)
