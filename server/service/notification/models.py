from server.manage.switch.models import *


class Notification_Model(Abstract_Model):

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20)
    date = models.DateField()
    direct_url = models.URLField()
    not_viewed = models.BooleanField(default=True)

    class Meta:
       unique_together = ('direct_url', 'type',)
