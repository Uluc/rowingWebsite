from django.contrib import admin
from .models import Rower, Race, Leadership, Event, Sponsor, Picture, Gallery, HomePage, SponsorPage, RecruitmentPage, AboutPage
from image_cropping.admin import ImageCroppingMixin
from adminsortable2.admin import SortableAdminMixin
from imagekit.admin import AdminThumbnail
from django.utils.html import format_html

admin.site.site_header="LSU Rowing Website Manager"

class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ['get_name','crew', 'orientation']

    def get_name(self, obj):
        if obj.first_name:
            return obj.first_name + " " + obj.last_name
        else:
            return 'Not Available'


    get_name.short_description = 'Rower'

class AdminGallery(ImageCroppingMixin, admin.ModelAdmin):
    pass

class MyModelAdminSorting(SortableAdminMixin, ImageCroppingMixin, admin.ModelAdmin):
    pass

class FancyAdmin(admin.ModelAdmin):
    list_display = ['description', 'asociated_event', 'image_display']
    image_display = AdminThumbnail(image_field='image_thumbnail')
    image_display.short_description = 'Image'

    # set this to also show the image in the change view
    readonly_fields = ['image_display']

admin.site.register(HomePage)
admin.site.register(SponsorPage)
admin.site.register(RecruitmentPage)
admin.site.register(AboutPage)
admin.site.register(Sponsor)
admin.site.register(Rower, MyModelAdmin)
admin.site.register(Race)
admin.site.register(Leadership, MyModelAdminSorting)
admin.site.register(Event)
admin.site.register(Picture, FancyAdmin)
admin.site.register(Gallery)


