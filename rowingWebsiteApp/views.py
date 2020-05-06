from django.shortcuts import render
from django.http import HttpResponse
from .models import Rowers
# Create your views here.

rowers = [
    {
        'name': 'Uluc Ozdenvar',
        'orientation': 'Starboard',
        'hometown': 'Istanbul, Turkey',
        'major': 'Computer Science'
    },
    {
        'name': 'Uluc Ozdenvar',
        'orientation': 'Starboard',
        'hometown': 'Istanbul, Turkey',
        'major': 'Computer Science'
    },
    {
        'name': 'Uluc Ozdenvar',
        'orientation': 'Starboard',
        'hometown': 'Istanbul, Turkey',
        'major': 'Computer Science'
    },
    {
        'name': 'Gerard Roeling',
        'orientation': 'Starboard',
        'hometown': 'Austin, TX',
        'major': 'ISDS'
    }
]

def home(request):
    return render(request, 'rowingWebsiteApp/homePage.htm', {'nbar': 'home'})

def roster(request):
    data = {
        'rowers': Rowers.objects.all(),
        'nbar': 'roster'
    }
    return render(request, 'rowingWebsiteApp/rosterPage.htm', data)

def schedule(request):
    return render(request, 'rowingWebsiteApp/schedulePage.htm', {'nbar': 'schedule'} )
    
def sponsor(request):
    return render(request, 'rowingWebsiteApp/sponsorPage.htm', {'nbar': 'sponsor'})

def recruitment(request):
    return render(request, 'rowingWebsiteApp/recruitmentPage.htm', {'nbar': 'recruitment'})

def leadership(request):
    return render(request, 'rowingWebsiteApp/leadershipPage.htm', {'nbar': 'leadership'})