from django.http import HttpResponse
from django.conf import settings
from sorl.thumbnail import get_thumbnail
from . models import ImageModerator


def image_moderator(request, path):
    try:
        size = request.GET.get('size', "150x100")
        img_obj = ImageModerator.objects.get(img_path=path)
        img_status = img_obj.approve_status
        if img_status == True:
            img = "%s/uploads/%s" % (settings.MEDIA_ROOT, path)
            img = get_thumbnail(img, size, crop='center', quality=99)
            img = "%s/%s" % (settings.MEDIA_ROOT, img.name)
        else:
            img = "%s/img/img-pending.gif" % (settings.MEDIA_ROOT)
    except Exception as e:
        print e.message
        img = "%s/img/img-not-found.jpg" % (settings.MEDIA_ROOT)

    with open(img, "rb") as f:
        return HttpResponse(f.read(), content_type="image/jpeg")