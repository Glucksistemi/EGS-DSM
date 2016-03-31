from utils.tcpclient import tcp_request
from utils.views import JsonView, prepare_date
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
import json
from utils.models import CoreLog


class AuthView(View):
    def post(self, request):
        data = json.loads(request.body)
        user = authenticate(username=data['login'], password=data['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('{"error": false}')
            return HttpResponse('{"error": "user is not active"}')
        return HttpResponse('{"error": "wrong login or password"}')


class AmIAuthorized(JsonView):
    def react(self, data):
        return {'unauthorized': False}


class RestartView(JsonView):
    def react(self, data):
        request = tcp_request('sne do')


class CoreLogView(JsonView):
    def react(self, data):
        print CoreLog.objects.all()[0:100].values()
        return [prepare_date(line) for line in CoreLog.objects.all()[0:100].values()]
