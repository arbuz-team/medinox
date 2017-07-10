from server.manage.switch.website.manager import *
from server.service.payment.models import *
from server.manage.root.models import *
from server.service.translator.views import *
from weasyprint import HTML


class Generator_PDF(Website_Manager):

    def Invoice(self, pk):

        payment = SQL.Get(Payment, pk=pk)
        address = SQL.Get(Invoice_Address, payment=payment)
        products = SQL.Filter(Selected_Product, payment=payment)
        seller = SQL.First(Root_Address)

        self.content['invoice'] = {
            'unique':           payment.pk,
            'date':             payment.date,
            'delivery':         payment.delivery_price,
            'seller':           seller,
            'client':           address,
            'products':         products,
            'brutto_price':     float(payment.total_price),
        }

        html = self.Render_HTML('pdf/invoice.html')
        return self.Generate(html)

    def Generate(self, html):

        if not self.Check_Authorization():
            return HttpResponse('Its not for you')

        pdf = HTML(string=html.content.decode()).write_pdf()

        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="{0}"'\
            .format(Text(self, 130))

        return response

    def Check_Authorization(self):

        if self.authorization:
            return True

        if self.request.session['root_login']:
            return True

        if not self.request.session['user_login']:
            return False

        payment = SQL.Get(Payment, pk=self.other_value)
        if self.request.session['user_user'] == payment.user:
            return True

        return False

    @staticmethod
    def Launch_Invoice(request, pk):
        return Generator_PDF(request, other_value=pk).Invoice(pk)

    @staticmethod
    def Launch(request):
        pass
