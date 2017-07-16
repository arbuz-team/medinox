from server.page.navigation.views import *
from server.page.searcher.views import *
from django.views.decorators.csrf import csrf_exempt

class Json_Example:

    @staticmethod
    @csrf_exempt
    def Launch(request):
        Check_Session(request)

        if '__content__' in request.POST:

            contents = request.POST['__content__'].split(' ')
            data = lambda x: {'status': x.status_code, 'html': x.content.decode('utf-8')}

            content = {
                'cart':         {'status': 200, 'html': 'Tu powinien być koszyk'},
                'navigation':   data(Navigation(request).Manage_Content_Navigation()),
                'header':       data(Navigation(request).Manage_Content_Header()),
                'searcher':     data(Searcher(request).Manage_Content_Searcher()),
                'ground':       data(Start(request).Manage_Content_Ground()),
            }

            json = {
                '__content__': {a: content[a] for a in contents}
            }

            return JsonResponse(json)

        return HttpResponse('Hue hue hue')
