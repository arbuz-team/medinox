from server.service.payment.models import *
from server.manage.root.models import *
from server.service.translator.views import *
from weasyprint import HTML


class Generator_PDF(Base):

    def Invoice(self):

        payment = SQL.Get(Model_Payment, pk=self.invoice_pk)
        client = SQL.Get(Model_Invoice_Address, payment=payment)
        products = SQL.Filter(Model_Payment_Product, payment=payment)
        seller = SQL.First(Model_Root_Address)

        self.context['payment'] = payment
        self.context['seller'] = seller
        self.context['client'] = client
        self.context['products'] = products

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

        payment = SQL.Get(Model_Payment, pk=self.invoice_pk)
        if self.request.session['user_user'] == payment.user:
            return True

        return False

    def __init__(self, request, pk, authorization=False):

        from server.manage.session.views import Check_Session
        Check_Session(request)

        self.authorization = authorization
        self.invoice_pk = pk
        self.request = request
        Base.__init__(self, self)

    @staticmethod
    def Launch(request, pk):
        return Generator_PDF(request, pk).Invoice()
