from server.manage.switch.website.base import *
from server.ground.product.models import *


class Sort_By_Price(Base):

    def Sort(self):

        # sort products
        order_by = ''
        direction = self.request.session['searcher_sort_direction']
        if direction == 'descending': order_by = '-price'
        if direction == 'ascending': order_by = 'price'

        return SQL.Filter(Model_Product,
            pk__in=self.products).order_by(order_by)

    def __init__(self, search_engine):
        Base.__init__(self, search_engine)
        self.products = search_engine.products
