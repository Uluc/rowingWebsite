from django.shortcuts import render
from django.http import HttpResponse
from .models import Race, Leadership, Event, Rower
from django.forms.models import model_to_dict
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.fields.files import ImageFieldFile
from image_cropping.utils import get_backend
# Create your views here.

class ExtendedEncoder(DjangoJSONEncoder):
    def default(self, o):
        if isinstance(o, ImageFieldFile):
            return str(o)
        else:
            return super().default(o)

def home(request):
    return render(request, 'rowingWebsiteApp/homePage.htm', {'nbar': 'home'})


def roster(request):
    nbar = 'roster'
    
    rower = Rower.objects.all()
    rowers = json.dumps([model_to_dict(item) for item in rower], cls=ExtendedEncoder)

    return render(request, 'rowingWebsiteApp/rosterPage.htm', {'nbar':nbar, 'rowers':rowers, 'rower':rower} )

def schedule(request):
    nbar = 'schedule'
    races = json.dumps([model_to_dict(item) for item in Race.objects.all()])
    return render(request, 'rowingWebsiteApp/schedulePage.htm',{'nbar':nbar, 'races':races} )
    
def sponsor(request):
    return render(request, 'rowingWebsiteApp/sponsorPage.htm', {'nbar': 'sponsor'})

def recruitment(request):
    nbar = 'recruitment'
    events = json.dumps([model_to_dict(item) for item in Event.objects.all()])
    return render(request, 'rowingWebsiteApp/recruitmentPage.htm', {'nbar':nbar, 'events':events})

def leadership(request):
    nbar = 'leadership'
    officers = json.dumps([model_to_dict(item) for item in Leadership.objects.all()], cls=ExtendedEncoder)
    return render(request, 'rowingWebsiteApp/leadershipPage.htm', {'nbar':nbar, 'officers': officers} )

