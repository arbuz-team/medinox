from .manager import *
from server.manage.switch.status import *


class Errors_Handler(Base):

    @staticmethod
    def CSRF_Failure(request, block=None):
        response_class = HttpResponseForbidden
        message = Text(request=request, pk=180)
        image = None
        return Errors_Handler(request, response_class,
                              message, image, block).HTML

    @staticmethod
    def Code_403(request, block=None):
        response_class = HttpResponseForbidden
        message = Text(request=request, pk=181)
        image = None
        return Errors_Handler(request, response_class,
                              message, image, block).HTML

    @staticmethod
    def Code_404(request, block=None):
        response_class = HttpResponseNotFound
        message = Text(request=request, pk=182)
        image = None
        return Errors_Handler(request, response_class,
                              message, image, block).HTML

    @staticmethod
    def Code_500(request, block=None):
        response_class = HttpResponseServerError
        message = Text(request=request, pk=183)
        image = None
        return Errors_Handler(request, response_class,
                              message, image, block).HTML

    def Get_Error_Block(self):

        blocks = self.request.session['arbuz_response'].keys()
        variables = self.request.POST.keys()
        error_blocks = []

        # only block variables
        for var in variables:
            if var.startswith('__') and var.endswith('__'):

                # find block variable
                # that not exist in created blocks
                if var not in blocks:
                    error_blocks.append(var)

        return error_blocks

    def Manage(self):

        response = self.request.session['arbuz_response']
        error_blocks = self.Get_Error_Block()

        # error block not found
        if not error_blocks:
            return HttpResponse('I don\'t know, which '
                                'block generate problem.')

        # all of error blocks
        for block in error_blocks:

            # generate error html
            response_html = self.blocks[block]\
                .Error(self.response_class, self.context)

            # append error html to response
            response[block] = Direct_Block_Manager\
                .Packing(response_html)

        self.request.session['arbuz_response'] = {}
        return JsonResponse(response)

    def Initialize(self):

        status_manager = Status_Manager(self)
        status_manager.Timer_Start()

        # when app get selected block error
        if self.selected_block:
            self.HTML = self.blocks[self.selected_block]\
                .Error(self.response_class, self.context)

        else: self.HTML = self.Manage()
        status_manager.Display_Status(message='INTERNAL')

    def __init__(self, request, response_class, message, image, selected_block):

        self.selected_block = selected_block
        self.response_class = response_class
        self.request = request
        self.HTML = None

        self.blocks = {
            '__ground__': Ground_Block(self),
            '__cart__': Cart_Block(self),
            '__menu__': Menu_Block(self),
            '__menu_mobile__': Menu_Mobile_Block(self),
            '__searcher__': Searcher_Block(self),
            '__dialog__': Dialog_Block(self)
        }

        Base.__init__(self, self)

        self.context['message'] = message
        self.context['image'] = image
        self.Initialize()



def csrf_failure(request, reason=''):
    return Errors_Handler.CSRF_Failure(request)