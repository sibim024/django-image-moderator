from django.http import HttpResponse
from django.conf import settings
from sorl.thumbnail import get_thumbnail
from . models import ImageModerator
from django.views.generic import View


class ImageModeratorViewHandler(View):

    def resize_image(self, img, dimension, crop):
        try:
            if crop == 'center':
                img = get_thumbnail(img, dimension, crop='center')
            else:
                img = get_thumbnail(img, dimension)
            img = "%s/%s" % (settings.MEDIA_ROOT, img.name)
        except:
            img = "%s/image_moderator/img-not-found.jpg" % settings.MEDIA_ROOT
        return img

    def get(self, request, *args, **kwargs):
        self.img = ''
        self.path = self.kwargs.get('path', None)
        self.dimension = request.GET.get('size') if request.GET.get('size') else None
        self.crop = request.GET.get('crop') if request.GET.get('crop') else None

        try:
            img_obj = ImageModerator.objects.get(img_path=self.path)
            img_status = img_obj.approve_status
            if img_status is True:
                self.img = "%s/%s" % (settings.MEDIA_ROOT, self.path)
                if self.dimension:
                    self.img = self.resize_image(self.img, self.dimension, self.crop)
            else:
                self.img = "%s/image_moderator/img-pending.gif" % settings.MEDIA_ROOT
                if self.dimension:
                    self.img = self.resize_image(self.img, self.dimension, self.crop)
        except Exception as e:
            self.img = "%s/image_moderator/img-not-found.jpg" % settings.MEDIA_ROOT
            if self.dimension:
                self.img = self.resize_image(self.img, self.dimension, self.crop)

        with open(self.img, "rb") as f:
            return HttpResponse(f.read(), content_type="image/jpeg")
