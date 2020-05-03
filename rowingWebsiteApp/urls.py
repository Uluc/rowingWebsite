from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='website-home'),
    path('roster/', views.roster, name='website-roster'),
    path('schedule/', views.schedule, name='website-schedule'),
    path('sponsor/', views.sponsor, name='website-sponsor'),
    path('recruitment/', views.recruitment, name='website-recruitment'),

]