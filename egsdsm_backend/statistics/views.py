from utils.views import JsonView
from utils.models import HeartBeat
from django.forms.models import model_to_dict
# Create your views here.


class HeartBeatView(JsonView):
    def react(self, data):
        return model_to_dict(HeartBeat.objects.latest('datetime'), exclude='datetime')