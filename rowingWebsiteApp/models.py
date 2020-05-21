from django.db import models
import zipfile
from image_cropping.fields import ImageRatioField, ImageCropField
from django.conf import settings
from easy_thumbnails.fields import ThumbnailerImageField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField
from zipfile import ZipFile
from sortedm2m.fields import SortedManyToManyField
from django.core.files.base import ContentFile
from django.utils.html import format_html
from django.utils.html import escape

# Create your models here.

class Rower(models.Model):

    ORIENTATION = (
        ('Starboard','Starboard'),
        ('Port', 'Port'),
        ('Bisweptual', 'Bisweptual'),
        ('Coxswain', 'Coxswain')
        )
    
    CREWS = (
        ('Mens', 'Mens'),
        ('Womens', 'Womens')
        )

    VARSITY = (
        ('Yes', 'Yes'),
        ('No', 'No')
        )
    
    YEAR = (
        ('Freshmen','FR'),
        ('Sophomore','SO'),
        ('Junior','JR'),
        ('Senior','SR')
    )

    first_name = models.CharField(max_length=64, blank=False)
    last_name = models.CharField(max_length=64)
    orientation = models.CharField(max_length=64, choices=ORIENTATION)
    hometown = models.CharField(max_length=64, help_text=("Example: Baton Rouge, LA"))
    major = models.CharField(max_length=64)
    picture = models.ImageField(upload_to = 'rowingWebsite/rowingWebsiteApp/media/')
    cropping = ImageRatioField('picture', '5x7')
    crew = models.CharField(max_length=64, choices=CREWS)
    varsity = models.CharField(max_length=64, choices=VARSITY)
    year = models.CharField(max_length=64, choices=YEAR)


    #displays the name
    def __str__(self):
        return self.first_name +" "+ self.last_name

    class Meta:
        ordering = ['last_name']

class Race(models.Model):

    SEMESTER = (
        ('Fall','Fall'),
        ('Spring','Spring'),
    )
    
    name = models.CharField(max_length=64)
    location= models.CharField(max_length=64, help_text=("Event address ex: 3355 Dalrymple Dr, Baton Rouge, LA 70802"))
    date = models.DateField(null=True, blank=True)
    semester = models.CharField(max_length=64, choices=SEMESTER)
    results = models.CharField(max_length=256, default='-', help_text=("Put the link to regatta central here once"))

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.name

class Event(models.Model):
    
    event = models.CharField(max_length=64)
    location= models.CharField(max_length=64, help_text=("Event address ex: 3355 Dalrymple Dr, Baton Rouge, LA 70802"))
    date = models.DateField(null=True, blank=True, help_text=("Select a date from the picker."))
    time= models.CharField(max_length=64, help_text=("Example: 3pm - 5pm"))

    def __str__(self):
        return self.event

class Leadership(models.Model):
    
    STAFF = (
        ('Officer','Officer'),
        ('Coach', 'Coach'),
    )

    name = models.CharField(max_length=64)
    position = models.CharField(max_length=64)
    staff = models.CharField(max_length=64, choices=STAFF, default='Officer')
    picture = models.ImageField(upload_to = 'rowingWebsite/rowingWebsiteApp/media/')
    cropping = ImageRatioField('picture', '5x5')
    writeUp = models.TextField(help_text=("This will be the text that get displayed under the officer"))
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['my_order']

    #displays the name
    def __str__(self):
        return self.name

class Sponsor(models.Model):
    
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    def __str__(self):
        return self.first_name + " " + self.last_name
    
    class Meta:
        ordering = ['last_name']

class Picture(models.Model):
    
    asociated_event = models.CharField(max_length=64, default='Picture', help_text=("Source of the event"))
    description = models.CharField(max_length=64, default='Picture', help_text=
    ("Describe your images so they can easily be identified to be added into appropriate gallery "))
    
    image = models.ImageField(upload_to='images')
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(125, 125)], format='JPEG', options={'quality': 80})

    def __str__(self):
        return self.asociated_event + " - " + self.description

class Gallery(models.Model):
    title = models.CharField(max_length=64, help_text=("Name for the gallery"))
    date = models.DateField(help_text=("Date the event occured"))
    images = SortedManyToManyField(Picture)

    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "Gallery"
        verbose_name_plural = "Galleries"
        ordering = ['-date']

class HomePage(models.Model):
    
    title = models.CharField(max_length=32)
    text = models.TextField(help_text=("This will be the text that gets displayed"))
    image = models.ImageField(upload_to='template_photos')

    class Meta:
        verbose_name_plural = "Home Page Entries"

class RecruitmentPage(models.Model):

    title = models.CharField(max_length=32)
    text = models.TextField(help_text=("This will be the text that gets displayed"))
    questionaire_link = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = "Recruitment Page Entries"

class SponsorPage(models.Model):
    title = models.CharField(max_length=32)
    text = models.TextField(help_text=("This will be the text that gets displayed"))
    sponsorship_coordinator_name = models.CharField(max_length=64)
    sponsorship_coordinator_email = models.EmailField(max_length=254, help_text=("Refer to LSU email"))
    image = models.ImageField(upload_to='template_photos')

    class Meta:
        verbose_name_plural = "Sponsor Page Entries"

