from datetime import datetime
from django.db.models import signals
from django.utils.functional import curry
from image_moderator.models import ImageModerator


class ImageModeratorMiddleware(object):

    def process_request(self, request):
        if request.method in ('POST', 'PUT', 'PATCH'):
            if hasattr(request, 'user') and request.user.is_authenticated():
                user = request.user
                image_moderation_handler = curry(self.image_moderation_handler, user)
                signals.post_save.connect(image_moderation_handler,  dispatch_uid=(self.__class__, request,), weak=False)

    def process_response(self, request, response):
        signals.post_save.disconnect(dispatch_uid=(self.__class__, request,))
        return response

    def image_moderation_handler(self, user, sender, instance, **kwargs):
        for field in instance._meta.fields:
            img_type = str(field.description)
            if img_type == "Image":
                img_field = field.attname
                file_name = getattr(instance, img_field).name
                if file_name:
                    app_label = instance._meta.model_name
                    model = instance._meta.object_name
                    modified_by = user.id
                    modified_on = datetime.now()
                    ImageModerator.objects.update_or_create(img_path=file_name,
                                                            defaults={
                                                                "app_label": app_label,
                                                                "model": model,
                                                                "modified_by": modified_by,
                                                                "modified_on": modified_on,
                                                                "approve_status": False
                                                            })
