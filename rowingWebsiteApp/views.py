from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'rowingWebsiteApp/homePage.htm', {'nbar': 'home'})

def roster(request):
    return render(request, 'rowingWebsiteApp/rosterPage.htm', {'nbar': 'roster'})

def schedule(request):
    return render(request, 'rowingWebsiteApp/schedulePage.htm', {'nbar': 'schedule'} )
    
def sponsor(request):
    return render(request, 'rowingWebsiteApp/sponsorPage.htm', {'nbar': 'sponsor'})

def recruitment(request):
    return render(request, 'rowingWebsiteApp/recruitmentPage.htm', {'nbar': 'recruitment'})

def leadership(request):
    return render(request, 'rowingWebsiteApp/leadershipPage.htm', {'nbar': 'leadership'})