from server.ground.product.models import *
from server.manage.root.models import Delivery


class Payment(Abstract_Model):

    user = models.ForeignKey(User)
    date = models.DateField()
    total_price = models.CharField(max_length=10)
    delivery_price = models.FloatField()
    currency = models.CharField(max_length=3)
    service = models.CharField(max_length=10)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

    def Update_Total_Price(self, _object):

        total = self.delivery_price
        selected_products = SQL.Filter(
            Payment_Product, payment=self)

        for selected in selected_products:
            product_price = selected.product.price.Get_Price(_object)
            total += product_price * selected.number

        self.total_price = format(total, '.2f')
        SQL.Save(data=self)

    @staticmethod
    def Initialize(_object, user):

        payments = SQL.Filter(Payment,
              user=user, status='cart')

        if payments.count() > 1:
            SQL.Delete(data=payments)

        if not payments:

            # delivery prices for first user address
            delivery = Delivery.Get_Price(_object)
            payment = Payment(
                user=user,
                date=datetime.today().date(),
                total_price='0.00',
                delivery_price=delivery,
                service='None',
                currency=_object.request.session['currency_selected'],
                status='cart'
            )

            SQL.Save(data=payment)



class Payment_Product(Abstract_Model):

    payment = models.ForeignKey(Payment)
    product = models.ForeignKey(Product)
    values = models.ManyToManyField(Values)
    number = models.IntegerField()

    def __str__(self):
        return self.product.name
