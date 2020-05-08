from django.shortcuts import render
from django.http import HttpResponse
from .models import Race, Leadership, Event, Rower
from django.forms.models import model_to_dict
import json
# Create your views here.


def home(request):
    return render(request, 'rowingWebsiteApp/homePage.htm', {'nbar': 'home'})

def roster(request):
    data = {
        'rower': Rower.objects.all(),
        'nbar': 'roster'
    }
    return render(request, 'rowingWebsiteApp/rosterPage.htm', data)

def schedule(request):
    data = {}
    data["races"] = json.dumps([model_to_dict(item) for item in Race.objects.all()])
    data['nbar'] =  'schedule'
    
    return render(request, 'rowingWebsiteApp/schedulePage.htm', data )
    
def sponsor(request):
    return render(request, 'rowingWebsiteApp/sponsorPage.htm', {'nbar': 'sponsor'})

def recruitment(request):
    return render(request, 'rowingWebsiteApp/recruitmentPage.htm', {'nbar': 'recruitment'})

def leadership(request):
    return render(request, 'rowingWebsiteApp/leadershipPage.htm', {'nbar': 'leadership'})