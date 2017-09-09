from .payment import *


class Model_Note(Abstract_Model):

    payment = models.OneToOneField(Model_Payment)
    note = models.TextField()

    @staticmethod
    def Initialize(payment):

        order_notes = SQL.Filter(
            Model_Note, payment=payment)

        if order_notes.count() > 1:
            SQL.Delete(data=order_notes)

        if not order_notes:
            SQL.Save(Model_Note,
                note='',
                payment=payment
            )



class Model_Note_File(Abstract_Model):

    name = models.CharField(max_length=50)
    file = models.FileField()
    note = models.ForeignKey(Model_Note)

    def Set_Variables(self):
        self.file_dir = 'files/orders/'