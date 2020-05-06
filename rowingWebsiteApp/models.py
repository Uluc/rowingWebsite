from django.db import models

# Create your models here.
class Rowers(models.Model):
    name = models.TextField()
    orientation = models.TextField()
    hometown = models.TextField()
    major = models.TextField()