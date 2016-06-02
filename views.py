from django.http import HttpResponse
from django.conf import settings
from sorl.thumbnail import get_thumbnail
from . models import ImageModerator

def crop_image(img, size):
    img = get_thumbnail(img, size, quality=99)
    img = "%s/%s" % (settings.MEDIA_ROOT, img.name)
    return img

def image_moderator(request, path):
    try:
        img_obj = ImageModerator.objects.get(img_path=path)
        img_status = img_obj.approve_status
        if img_status == True:
            img = "%s/%s" % (settings.MEDIA_ROOT, path)
            if request.GET.get('size'):
                size = request.GET.get('size')
                img = crop_image(img, size)
        else:
            img = "%s/image_moderator/img-pending.gif" % (settings.STATIC_ROOT)
    except Exception as e:
        img = "%s/image_moderator/img-not-found.jpg" % (settings.STATIC_ROOT)

    with open(img, "rb") as f:
        return HttpResponse(f.read(), content_type="image/jpeg")