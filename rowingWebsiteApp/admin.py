from django.contrib import admin
from django.contrib.admin import sites
from .models import Rower, Race, Leadership, Event, Sponsor, Picture, Gallery, HomePage, SponsorPage, RecruitmentPage, AboutPage
from image_cropping.admin import ImageCroppingMixin
from adminsortable2.admin import SortableAdminMixin
from imagekit.admin import AdminThumbnail
from django.utils.html import format_html

admin.site.site_header="LSU Rowing Website Manager"

class NoDeleteAdminMixin:
    def has_delete_permission(self, request, obj=None):
        return False
    def has_add_permission(self, request):
        return False

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
    list_display = ['name', 'position', 'staff']

class FancyAdmin(admin.ModelAdmin):
    list_display = ['description', 'asociated_event', 'image_display']
    image_display = AdminThumbnail(image_field='image_thumbnail')
    image_display.short_description = 'Image'

    # set this to also show the image in the change view
    readonly_fields = ['image_display']

class RecruitmentAdmin(NoDeleteAdminMixin, admin.ModelAdmin):
    pass

class SponsorAdmin(NoDeleteAdminMixin, admin.ModelAdmin):
    pass

admin.site.register(HomePage)
admin.site.register(SponsorPage, SponsorAdmin)
admin.site.register(RecruitmentPage, RecruitmentAdmin)
admin.site.register(AboutPage)
admin.site.register(Sponsor)
admin.site.register(Rower, MyModelAdmin)
admin.site.register(Race)
admin.site.register(Leadership, MyModelAdminSorting)
admin.site.register(Event)
admin.site.register(Picture, FancyAdmin)
admin.site.register(Gallery)


