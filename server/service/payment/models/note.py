from .payment import *


class Model_Order_Note(Abstract_Model):

    payment = models.OneToOneField(Model_Payment)
    note = models.TextField()

    @staticmethod
    def Initialize(payment):

        order_notes = SQL.Filter(
            Model_Order_Note, payment=payment)

        if order_notes.count() > 1:
            SQL.Delete(data=order_notes)

        if not order_notes:
            SQL.Save(Model_Order_Note,
                note='',
                payment=payment
            )



class Note_File(Abstract_Model):

    name = models.CharField(max_length=50)
    file = models.FileField()
    note = models.ForeignKey(Model_Order_Note)

    def Set_Variables(self):
        self.file_dir = 'files/orders/'