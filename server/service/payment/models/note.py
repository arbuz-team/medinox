from .payment import *


class Order_Note(Abstract_Model):

    payment = models.OneToOneField(Payment)
    note = models.TextField()

    @staticmethod
    def Initialize(payment):

        order_notes = SQL.Filter(
            Order_Note, payment=payment)

        if order_notes.count() > 1:
            SQL.Delete(data=order_notes)

        if not order_notes:
            SQL.Save(Order_Note,
                note='',
                payment=payment
            )



class Note_File(Abstract_Model):

    name = models.CharField(max_length=50)
    file = models.FileField()
    note = models.ForeignKey(Order_Note)

    def Set_Variables(self):
        self.file_dir = 'files/orders/'