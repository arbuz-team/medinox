from server.manage.switch.models import *


class Model_Notification(Abstract_Model):

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20)
    date = models.DateField()
    direct_url = models.URLField()
    not_viewed = models.BooleanField(default=True)

    class Meta:
       unique_together = ('direct_url', 'type',)

    @staticmethod
    def Create_Deadline_Notification(_object, deadline):
        today = datetime.today()
        path_manager = Path_Manager(_object)

        SQL.Save(
            Model_Notification,
            name=deadline.name,
            type='deadline',
            date=today,
            direct_url=path_manager.Get_Urls(
                'root.selected_user_payment',
                kwargs={'pk': deadline.payment.pk},
                current_language=True
            )
        )

    @staticmethod
    def Create_Reminder_Notification(_object, reminder):
        today = datetime.today()
        path_manager = Path_Manager(_object)

        SQL.Save(
            Model_Notification,
            name=reminder.name,
            type='reminder',
            date=today,
            direct_url=path_manager.Get_Urls(
                'root.selected_user_payment',
                kwargs={'pk': reminder.payment.pk},
                current_language=True
            )
        )
