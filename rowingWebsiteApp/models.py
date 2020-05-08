from django.db import models

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
        ('Yes', 'T'),
        ('No', 'F')
        )
    
    YEAR = (
        ('Freshmen','FR'),
        ('Sophmore','SO'),
        ('Junior','JR'),
        ('Senior','SR')
    )

    name = models.CharField(max_length=64)
    orientation = models.CharField(max_length=64, choices=ORIENTATION)
    hometown = models.CharField(max_length=64)
    major = models.CharField(max_length=64)
    picture = models.ImageField(upload_to = 'rowingWebsite/rowingWebsiteApp/media/', default = 'pic_folder/None/no-img.jpg')
    crew = models.CharField(max_length=64, choices=CREWS)
    varsity = models.CharField(max_length=64, choices=VARSITY)
    year = models.CharField(max_length=64, choices=YEAR)


    #displays the name
    def __str__(self):
        return self.name

class Race(models.Model):

    SEMESTER = (
        ('Fall','Fall'),
        ('Spring','Spring'),
    )
    
    name = models.CharField(max_length=64)
    location= models.CharField(max_length=64)
    date = models.CharField(max_length=64)
    semester = models.CharField(max_length=64, choices=SEMESTER)
    results = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Event(models.Model):
    
    event = models.CharField(max_length=64)
    location= models.CharField(max_length=64)
    date_and_time = models.CharField(max_length=64, default="To Be Announced")

    def __str__(self):
        return self.event

class Leadership(models.Model):
    
    name = models.CharField(max_length=64)
    position = models.CharField(max_length=64)
    picture = models.ImageField(upload_to = 'rowingWebsite/rowingWebsiteApp/media/', default = 'pic_folder/None/no-img.jpg')
    writeUp = models.TextField()

    #displays the name
    def __str__(self):
        return self.name
