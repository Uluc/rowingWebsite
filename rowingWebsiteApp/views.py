from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'rowingWebsiteApp/homePage.htm')

def roster(request):
    return render(request, 'rowingWebsiteApp/rosterPage.htm')

def schedule(request):
    return render(request, 'rowingWebsiteApp/schedulePage.htm')
    
def sponsor(request):
    return render(request, 'rowingWebsiteApp/sponsorPage.htm')

def recruitment(request):
    return render(request, 'rowingWebsiteApp/recruitmentPage.htm')

def leadership(request):
    return render(request, 'rowingWebsiteApp/leadershipPage.htm')