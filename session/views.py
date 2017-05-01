from inspect import getmembers, ismethod
from translator.views import *
from product.models import *
from root.models import *


class Session_Controller:

    def Check_Session_Arbuz(self):

        if 'arbuz_navigation' not in self.request.session:
            self.request.session['arbuz_navigation'] = []

        if 'arbuz_url' not in self.request.session:
            self.request.session['arbuz_url'] = {}

        if 'arbuz_permissions' not in self.request.session:
            self.request.session['arbuz_permissions'] = ''

        if 'arbuz_app' not in self.request.session:
            self.request.session['arbuz_app'] = ''

    def Check_Session_User(self):

        if 'user_login' not in self.request.session:
            self.request.session['user_login'] = False

        if 'user_unique' not in self.request.session:
            self.request.session['user_unique'] = 0

        if 'user_username' not in self.request.session:
            self.request.session['user_username'] = ''

        if 'user_my_shopping_date_from' not in self.request.session:
            self.request.session['user_my_shopping_date_from'] = \
                (datetime.today() - timedelta(days=7)).strftime('%Y-%m-%d')

        if 'user_my_shopping_date_to' not in self.request.session:
            self.request.session['user_my_shopping_date_to'] = \
                datetime.today().strftime('%Y-%m-%d')

    def Check_Session_Root(self):

        if 'root_login' not in self.request.session:
            self.request.session['root_login'] = False

        if 'root_payments_approved' not in self.request.session:
            self.request.session['root_payments_approved'] = True

        if 'root_users_payments_date_from' not in self.request.session:
            self.request.session['root_users_payments_date_from'] = \
                (datetime.today() - timedelta(days=7)).strftime('%Y-%m-%d')

        if 'root_users_payments_date_to' not in self.request.session:
            self.request.session['root_users_payments_date_to'] = \
                datetime.today().strftime('%Y-%m-%d')

        if 'root_address' not in self.request.session:
            self.request.session['root_address'] = \
                Root_Address.objects.first()

        if 'root_social_media' not in self.request.session:
            self.request.session['root_social_media'] = \
                Social_Media.objects.all()

    def Check_Session_Translator(self):

        if 'translator_language' not in self.request.session:
            self.request.session['translator_language'] = 'EN'

        if 'translator_currency' not in self.request.session:
            self.request.session['translator_currency'] = 'EUR'

        Translator.Set_Subdomain_Language(self.request)
        Translator.Set_Currency(self.request)

    def Check_Session_Product(self):

        if 'product_details_en' not in self.request.session:
            details = Details_EN(name='', description='')
            self.request.session['product_details_en'] = details
            self.request.session['product_details_en'].save()

        if 'product_details_pl' not in self.request.session:
            details = Details_PL(name='', description='')
            self.request.session['product_details_pl'] = details
            self.request.session['product_details_pl'].save()

        if 'product_details_de' not in self.request.session:
            details = Details_DE(name='', description='')
            self.request.session['product_details_de'] = details
            self.request.session['product_details_de'].save()

        if 'product_where_display' not in self.request.session:
            self.request.session['product_where_display'] = \
                Where_Display.objects.get(display_en=True,
                      display_pl=True, display_de=True)

        if 'product_brand' not in self.request.session:
            self.request.session['product_brand'] = None

        if 'product_purpose' not in self.request.session:
            self.request.session['product_purpose'] = {}

        if 'product_image' not in self.request.session:
            self.request.session['product_image'] = None

        if 'product_image_url' not in self.request.session:
            self.request.session['product_image_url'] = None

    def Check_Session_Searcher(self):

        if 'searcher_filter_brand' not in self.request.session:
            self.request.session['searcher_filter_brand'] = []

        if 'searcher_filter_purpose' not in self.request.session:
            self.request.session['searcher_filter_purpose'] = []

        if 'searcher_phrase' not in self.request.session:
            self.request.session['searcher_phrase'] = ''

        if 'searcher_order_name' not in self.request.session:
            self.request.session['searcher_order_name'] = 'search_accuracy'

        if 'searcher_order_direction' not in self.request.session:
            self.request.session['searcher_order_direction'] = 'descending'

        if 'searcher_result' not in self.request.session:
            self.request.session['searcher_result'] = Product.objects.all()

    def Check_Session_Main(self):

        if 'main_content_tab' not in self.request.session:
            self.request.session['main_content_tab'] = ''

        if 'main_page' not in self.request.session:
            self.request.session['main_page'] = 1

        if 'main_number_product_on_page' not in self.request.session:
            self.request.session['main_number_product_on_page'] = 10

    def Check_Session(self):

        methods = getmembers(self, predicate=ismethod)
        methods = [method[0] for method in methods]

        for method in methods:
            if 'Check_Session_' in method:
                getattr(Session_Controller, method)(self)


    def __init__(self, request):
        self.request = request
        self.Check_Session()



def Check_Session(request):
    Session_Controller(request)