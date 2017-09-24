from server.ground.product.models import *
from server.manage.root.models import Model_Delivery


class Model_Payment(Abstract_Model):

    user = models.ForeignKey(Model_User)
    date = models.DateField()
    total_price = models.CharField(max_length=10)
    delivery_price = models.FloatField()
    delivery_method = models.CharField(max_length=20)
    currency = models.CharField(max_length=3)
    service = models.CharField(max_length=20)
    status = models.CharField(max_length=20) # group
    unique = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

    def Update_Total_Price(self, _object):

        total = self.delivery_price
        selected_products = SQL.Filter(
            Model_Payment_Product, payment=self)

        for selected in selected_products:
            currency_manager = Base_Currency_Manager(_object)
            product_price = currency_manager.Get_Price(selected.product.price)
            total += product_price * selected.number

        self.total_price = format(total, '.2f')
        SQL.Save(data=self)

    @staticmethod
    def Generate_Unique():

        unique = Base.Generate_Random_Chars(
            20, punctuation=False)

        if SQL.Filter(Model_Payment, unique=unique):
            return Model_Payment.Generate_Unique()

        return unique

    @staticmethod
    def Initialize(_object, user):

        payments = SQL.Filter(Model_Payment,
              user=user, status='cart')

        if payments.count() > 1:
            SQL.Delete(data=payments)

        if not payments:

            # delivery prices for first user address
            payment = Model_Payment(
                user=user,
                date=datetime.today().date(),
                total_price='0.00',
                delivery_price=0,
                service='None',
                currency=_object.request.session['currency_selected'],
                status='cart',
                unique=Model_Payment.Generate_Unique()
            )

            SQL.Save(data=payment)



class Model_Payment_Product(Abstract_Model):

    payment = models.ForeignKey(Model_Payment)
    product = models.ForeignKey(Model_Product)
    values = models.ManyToManyField(Model_Values)
    number = models.IntegerField()

    def __str__(self):
        return self.product.name
