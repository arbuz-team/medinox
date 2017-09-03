from .payment import *


class Order_Deadline(Abstract_Model):

    payment = models.OneToOneField(Payment)
    name = models.CharField(max_length=20)
    deadline = models.DateField(null=True)
    send_to_buyer = models.BooleanField()
    send_to_root = models.BooleanField()
    reminder = models.DateField(null=True)

    @staticmethod
    def Initialize(payment):

        order_deadline = SQL.Filter(
            Order_Deadline, payment=payment)

        if order_deadline.count() > 1:
            SQL.Delete(data=order_deadline)

        if not order_deadline:
            SQL.Save(Order_Deadline,
                name='',
                send_to_buyer=False,
                send_to_root=False,
                payment=payment
            )
