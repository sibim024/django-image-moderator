from django.db import models


class ImageModerator(models.Model):
    class Meta:
        verbose_name = "image"
        verbose_name_plural = "images"
        db_table = "image_moderator"

    img_path = models.CharField(max_length=200, verbose_name="Image path", null=True)
    app_label = models.CharField(max_length=50, null=True)
    model = models.CharField(max_length=50, null=True)
    approve_status = models.BooleanField(verbose_name="Image status", default=False)
    modified_on = models.DateTimeField(auto_now=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)

    def image_thumb(self):
        if self.img_path:
            return u'<img src="/static/media/uploads/%s" style="width: 150px;" />' % self.img_path
        else:
            return 'No Image Found'
    image_thumb.short_description = 'Image'
    image_thumb.allow_tags = True

    def image_medium(self):
        if self.img_path:
            return u'<img src="/static/media/uploads/%s" style="width: 450px;" />' % self.img_path
        else:
            return 'No Image Found'
    image_medium.short_description = 'Image'
    image_medium.allow_tags = True

    def __unicode__(self):
        return self.model
