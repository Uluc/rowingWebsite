from django.contrib import admin
from .models import Rower, Race, Leadership, Event
from image_cropping import ImageCroppingMixin

class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

admin.site.register(Rower, MyModelAdmin)
admin.site.register(Race)
admin.site.register(Leadership, MyModelAdmin)
admin.site.register(Event)
# Register your models here.
