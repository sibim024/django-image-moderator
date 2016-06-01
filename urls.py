from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^image_moderator/(?P<path>.+)/$', views.image_moderator)
]