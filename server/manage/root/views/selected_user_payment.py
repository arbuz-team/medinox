from server.manage.switch.website.manager import *
from server.service.payment.forms import *


class Selected_User_Payment(Website_Manager):

    def Create_Payment_Structure(self):
        payment = SQL.Get(Payment, pk=self.other_value)

        self.context['shopping'] = [{
            'fullname': SQL.Get(Invoice_Address, payment=payment).full_name,
            'payment':  payment,
            'products': SQL.Filter(Selected_Product, payment=payment)
        }]

    def Manage_Content(self):

        path_manager = Path_Manager(self)
        notifications = SQL.Filter(Notification_Model, direct_url=\
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
