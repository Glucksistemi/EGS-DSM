from django.views.generic import View
from django.http import HttpResponse
import json


class JsonView(View):
    """
    wrapper around json send/get
    """
    request = None

    def react(self, data):
        pass

    def post(self, request):
        self.request = request
        if request.user.is_authentificated():
            return HttpResponse(json.dumps(self.react(json.loads(request.POST['json']))))  # May require sending request
        else:
            return HttpResponse('{"unauthorized": true}')

    def get(self, request):
        return HttpResponse(
            json.dumps(
                {
                    'error': 'wrong_http_method'
                }
            )
        )
