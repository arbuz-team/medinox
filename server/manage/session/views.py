from inspect import getmembers, ismethod
from server.service.currency.views.base import *
from server.ground.product.models import *
from server.manage.root.models import *


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

        if 'arbuz_response' not in self.request.session:
            self.request.session['arbuz_response'] = {}

        if 'arbuz_debug' not in self.request.session:
            self.request.session['arbuz_debug'] = DEBUG

    def Check_Session_User(self):

        if 'user_login' not in self.request.session:
            self.request.session['user_login'] = False

        if 'user_user' not in self.request.session:
            self.request.session['user_user'] = None

        if 'user_my_shopping_date_from' not in self.request.session:
            self.request.session['user_my_shopping_date_from'] = \
                (datetime.today() - timedelta(days=7)).strftime('%Y-%m-%d')

        if 'user_my_shopping_date_to' not in self.request.session:
            self.request.session['user_my_shopping_date_to'] = \
                datetime.today().strftime('%Y-%m-%d')

    def Check_Session_Root(self):

        if 'root_login' not in self.request.session:
            self.request.session['root_login'] = True

        if 'root_payment_status' not in self.request.session:
            self.request.session['root_payment_status'] = 'cart'

        if 'root_users_payments_date_from' not in self.request.session:
            self.request.session['root_users_payments_date_from'] = \
                (datetime.today() - timedelta(days=7)).strftime('%Y-%m-%d')

        if 'root_users_payments_date_to' not in self.request.session:
            self.request.session['root_users_payments_date_to'] = \
                datetime.today().strftime('%Y-%m-%d')

        if 'root_address' not in self.request.session:
            self.request.session['root_address'] = \
                SQL.First(Model_Root_Address)

        if 'root_social_media' not in self.request.session:
            self.request.session['root_social_media'] = \
                SQL.All(Model_Social_Media)

        if 'root_note' not in self.request.session:
            self.request.session['root_note'] = None

        if 'root_deadline' not in self.request.session:
            self.request.session['root_deadline'] = None

    def Check_Session_Translator(self):

        if 'translator_language' not in self.request.session:
            self.request.session['translator_language'] = 'EN'

        translator = Translator(self)
        translator.Set_Subdomain_Language()

    def Check_Session_Currency(self):

        if 'currency_selected' not in self.request.session:
            self.request.session['currency_selected'] = 'EUR'

            currency = Base_Currency_Manager(self)
            currency.Set_Default_Currency()

    def Check_Session_Product(self):

        if 'product_last_selected' not in self.request.session:
            self.request.session['product_last_selected'] = None

        if 'product_editing' not in self.request.session:
            self.request.session['product_editing'] = None

        if 'product_widget' not in self.request.session:
            self.request.session['product_widget'] = None

        if 'product_description' not in self.request.session:
            self.request.session['product_description'] = None

        if 'product_is_editing' not in self.request.session:
            self.request.session['product_is_editing'] = False

        if 'product_page' not in self.request.session:
            self.request.session['product_page'] = 1

        if 'product_number_on_page' not in self.request.session:
            self.request.session['product_number_on_page'] = 10

    def Check_Session_Catalog(self):

        if 'catalog_parent' not in self.request.session:
            self.request.session['catalog_parent'] = \
                SQL.Get(Model_Catalog, parent=None, name='/')

        if 'catalog_editing' not in self.request.session:
            self.request.session['catalog_editing'] = None

        if 'catalog_path' not in self.request.session:
            self.request.session['catalog_path'] = ''

        if 'catalog_selected_page' not in self.request.session:
            self.request.session['catalog_selected_page'] = 1

        if 'catalog_number_on_page' not in self.request.session:
            self.request.session['catalog_number_on_page'] = 8

        if 'catalog_copy_element' not in self.request.session:
            self.request.session['catalog_copy_element'] = None

        if 'catalog_move_element' not in self.request.session:
            self.request.session['catalog_move_element'] = None

        if 'catalog_move_type' not in self.request.session:
            self.request.session['catalog_move_type'] = ''

        if 'catalog_deleted_flag' not in self.request.session:
            self.request.session['catalog_deleted_flag'] = False

    def Check_Session_Searcher(self):

        if 'searcher_filter_brand' not in self.request.session:
            self.request.session['searcher_filter_brand'] = []

        if 'searcher_filter_purpose' not in self.request.session:
            self.request.session['searcher_filter_purpose'] = []

        if 'searcher_phrase' not in self.request.session:
            self.request.session['searcher_phrase'] = ''

        if 'searcher_sort_name' not in self.request.session:
            self.request.session['searcher_sort_name'] = 'search_accuracy'

        if 'searcher_sort_direction' not in self.request.session:
            self.request.session['searcher_sort_direction'] = 'descending'

        if 'searcher_result' not in self.request.session:
            self.request.session['searcher_result'] = SQL.All(Model_Product)

    def Check_Session_Main(self):

        if 'main_about' not in self.request.session:
            self.request.session['main_about'] = ''

        if 'main_home' not in self.request.session:
            self.request.session['main_home'] = ''

    def Check_Session_Notification(self):

        if 'notification_is_unreaded' not in self.request.session:
            self.request.session['notification_is_unreaded'] = False

    def Check_Session_Link(self):

        if 'link_editing' not in self.request.session:
            self.request.session['link_editing'] = None

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