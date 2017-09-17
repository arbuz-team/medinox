from server.manage.switch.website.manager import *
from server.service.payment.forms import *


class Selected_User_Payment(Website_Manager):

    def Create_Payment_Structure(self):
        payment = SQL.Get(Model_Payment, pk=self.other_value)

        self.context['shopping'] = [{
            'name': SQL.Get(Model_Invoice_Address, payment=payment).name,
            'surname': SQL.Get(Model_Invoice_Address, payment=payment).surname,
            'company_name': SQL.Get(Model_Invoice_Address, payment=payment).company_name,
            'payment':  payment,
            'products': SQL.Filter(Model_Payment_Product, payment=payment)
        }]

    def Manage_Content(self):

        path_manager = Path_Manager(self)
        notifications = SQL.Filter(Model_Notification, direct_url=\
            path_manager.Get_Urls(current_language=True))

        # notifications is viewed
        for notification in notifications:
            notification.not_viewed = False
            SQL.Save(data=notification)

        self.Create_Payment_Structure()
        self.context['button_address_name'] = 'root_address'
        return self.Render_HTML('root/selected_user_payment.html')

    @staticmethod
    def Launch(request, pk):
        return Selected_User_Payment(request, only_root=True, other_value=pk).HTML
