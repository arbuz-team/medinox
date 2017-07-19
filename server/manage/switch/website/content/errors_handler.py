from .block import *
from server.manage.switch.status import *


class Errors_Handler(Base_Website):

    @staticmethod
    def CSRF_Failure(request):
        Errors_Handler(request)
        return HttpResponse('csrf_failure')

    @staticmethod
    def Code_403(request):
        Errors_Handler(request)
        return HttpResponse('403')

    @staticmethod
    def Code_404(request):
        Errors_Handler(request)
        return HttpResponse('404')

    @staticmethod
    def Code_500(request):
        Errors_Handler(request)
        return HttpResponse('500')

    def __init__(self, request):
        self.request = request

        Base_Website.__init__(self, self)
        status = Status_Manager(self)
        status.Timer_Start()
        status.Display_Status(message='INTERNAL')



def csrf_failure(request, reason=""):
    return Errors_Handler.CSRF_Failure(request)