from django.contrib import admin
from .models import Rower, Race, Leadership, Event, Sponsors, Gallery
from image_cropping.admin import ImageCroppingMixin
from adminsortable2.admin import SortableAdminMixin

class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

class MyModelAdminSorting(SortableAdminMixin, ImageCroppingMixin, admin.ModelAdmin):
    pass

admin.site.register(Sponsors)
admin.site.register(Rower, MyModelAdmin)
admin.site.register(Race)
admin.site.register(Leadership, MyModelAdminSorting)
admin.site.register(Event)
admin.site.register(Gallery, MyModelAdmin)

# Register your models here.
