from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='website-home'),
    path('roster/', views.roster, name='website-roster'),
]