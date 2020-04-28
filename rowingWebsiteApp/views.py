from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('<h1>Website Home</h1>')

def roster(request):
    return HttpResponse('<h1>Website Roster</h1>')