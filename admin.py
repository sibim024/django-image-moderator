from django.contrib import admin
from .models import ImageModerator
from django.contrib.auth.models import User


def approve_images(modeladmin, request, queryset):
    queryset.update(approve_status=1)
approve_images.short_description = "Approve selected images"

def reject_images(modeladmin, request, queryset):
    queryset.update(approve_status=0)
reject_images.short_description = "Reject selected images"


class ImageModeratorAdmin(admin.ModelAdmin):
    list_display = ('image_thumb', 'img_path', 'app_label', 'model',
              'modified_on', 'get_username_from_userid', 'approve_status', )
    fields = ('image_medium', 'img_path', 'app_label', 'model',
              'modified_on', 'get_username_from_userid', 'approve_status', )
    readonly_fields = ('image_medium', 'img_path', 'app_label', 'model', 'modified_on', 'get_username_from_userid', )
    list_filter = ('model', )
    actions = (approve_images, reject_images, )

    def get_username_from_userid(self, obj):
        return u'%s' % User.objects.get(pk=obj.modified_by).username

    get_username_from_userid.short_description = 'Modified by'

    def has_add_permission(self, request):
        return False

    def get_actions(self, request):
        actions = super(ImageModeratorAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

admin.site.register(ImageModerator, ImageModeratorAdmin)
