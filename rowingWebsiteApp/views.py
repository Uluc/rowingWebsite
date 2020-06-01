from django.shortcuts import render
from django.http import HttpResponse
from .models import Race, Leadership, Event, Rower, Sponsor, Picture, Gallery, SponsorPage, HomePage, AboutPage, RecruitmentPage, PageBanners
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.fields.files import ImageFieldFile
from django.db.models import F  
from django.core.mail import send_mail



# Create your views here.

class ExtendedEncoder(DjangoJSONEncoder):
    def default(self, o):
        if isinstance(o, ImageFieldFile):
            return str(o)
        else:
            return super().default(o)

def aboutus(request):
    data={
        'nbar' : 'aboutus',
        'aboutText' : AboutPage.objects.all(),
        'banner' : PageBanners.objects.all()
    }
    return render(request, 'rowingWebsiteApp/aboutUsPage.htm', data)

def confirmed(request):
    return render(request, 'rowingWebsiteApp/confirmationPage.htm')

def home(request):
    nbar = 'home'
    homeText = HomePage.objects.all()

    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        send_mail(
            'Inquiry from ' + message_name,
            message,
            message_email,
            ['ulucozdenvar01@gmail.com'],
        )

        return render(request, 'rowingWebsiteApp/homePage.htm', {'nbar':nbar, 'homeText':homeText})
    else:
        return render(request, 'rowingWebsiteApp/homePage.htm', {'nbar':nbar, 'homeText':homeText})

def photogallery(request):
    data = {
        'nbar' : 'photos',
        'gallery' : Gallery.objects.all()
    }
    return render(request, 'rowingWebsiteApp/photoGalleryPage.htm', data )

def roster(request):
    data={
        'nbar' : 'roster' , 
        'rower' : Rower.objects.all()
    }
    return render(request, 'rowingWebsiteApp/rosterPage.htm', data)

def schedule(request):
    data = {
        'nbar' : 'schedule',
        'races' : Race.objects.all().order_by(F('date').asc(nulls_last=True)),
        'banner' : PageBanners.objects.all()
    }
    return render(request, 'rowingWebsiteApp/schedulePage.htm', data)
    
def sponsor(request):
    data = {
        'nbar' : 'sponsor',
        'sponsors' : Sponsor.objects.all(),
        'sponsorText' : SponsorPage.objects.all(),
        'banner' : PageBanners.objects.all()
    }
    return render(request, 'rowingWebsiteApp/sponsorPage.htm', data)

def recruitment(request):
    data = {
        'nbar' : 'recruitment',
        'events' : Event.objects.all(),
        'recruitmentText' : RecruitmentPage.objects.all(),
        'banner' : PageBanners.objects.all()
        
    }
    return render(request, 'rowingWebsiteApp/recruitmentPage.htm', data)

def leadership(request):
    data = {
        'nbar' : 'leadership',
        'leadership' : Leadership.objects.all()
    }
    return render(request, 'rowingWebsiteApp/leadershipPage.htm', data )



