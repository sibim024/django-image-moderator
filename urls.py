from django.conf.urls import url
from image_moderator.views import ImageModeratorViewHandler

urlpatterns = [
    url(r'^(?P<path>.+)/$', ImageModeratorViewHandler.as_view())
]