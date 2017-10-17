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

        # update products for invoice
        total = self.delivery_price
        products = SQL.Filter(Model_Payment_Product, payment=self)

        for product in products:
            product.Copy_Data_For_Invoice(_object)
            total += product.total_price * product.number

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

    # copy for invoice
    product_name = models.CharField(max_length=100)
    total_price = models.FloatField(default=0)

    def Copy_Data_For_Invoice(self, _object):

        from server.service.currency.views.base \
            import Base_Currency_Manager

        # save product name
        self.product_name = self.product.name

        # calculate total price
        manager = Base_Currency_Manager(_object)
        total = manager.Get_Price(self.product.price)

        for value in self.values.all():
            total += manager.Get_Price(value.super_price)

        # save total price
        self.total_price = total

        # save data
        SQL.Save(data=self)

    def __str__(self):
        return self.product.name
