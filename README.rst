===================
 django_imagemoderator
===================

django_imagemoderator is useful when there is a need to moderate images uploaded from any model. It recognizes image uploads from any model and provides a provision to approve / reject them from the django-admin backend. It also provides an API to view approved images. Rejected images will not be rendered in the API.


Requirements
============

<b>django_imagemoderator requires the following:</b>

Python 2.7<br>
Django 1.8+


Installation
=============

Install package dependency::

	$ sudo apt-get install libjpeg-dev
	$ sudo apt-get install libjpeg8-dev
	$ pip install sorl-thumbnail
	$ pip install Pillow

Add 'sorl.thumbnail', 'image_moderator' to your INSTALLED_APPS 
`settings.py` file::

INSTALLED_APPS = (
    ...
    'sorl.thumbnail',
    'image_moderator',
)

<b>Add middleware class to MIDDLEWARE_CLASSES setting:</b>

MIDDLEWARE_CLASSES = [
    ...
    'image_moderator.middleware.ImageModeratorMiddleware',
]

<b>Add the following urlpattern to your root urls.py file:</b>

urlpatterns = [
    ...
    url(r'^', include('image_moderator.urls'))
]

Example
========

In your App's models.py, specify image field as <b>ImageModeratorField()</b> instead of <b>models.ImageField()</b>:

```from image_moderator.models import ImageModeratorField```<br>

```class MyModel(models.Model):```</br>
```    image = ImageModeratorField(upload_to=upload_handler, blank=True, null=True)```


Now you can call the image API:

http://YOUR_DOMAIN_URL/image_moderator/IMAGE_NAME.jpg/?size=WIDTHxHEIGHT<br>
<b>Eg:</b> http://example.com/image_moderator/image.jpg/?size=300x200
