=======================
 Django Imagemoderator
=======================

Django Imagemoderator is used to moderate images uploaded from any model. It recognizes image fields from any model and provides a provision to approve / reject them from the django-admin backend. It also provides an API to view approved images. Rejected images will not be rendered in the API.


Requirements
============

django_imagemoderator requires the following::

	Python 2.7
	Django 1.8+


Installation
============

Install package dependency::

	$ sudo apt-get install libjpeg-dev
	$ sudo apt-get install libjpeg8-dev
	$ pip install sorl-thumbnail
	$ pip install Pillow

Add *'sorl.thumbnail'*, *'image_moderator'* to your INSTALLED_APPS settings file::

	INSTALLED_APPS = (
	    ...
	    'sorl.thumbnail',
	    'image_moderator',
	)

Add middleware class to MIDDLEWARE_CLASSES setting::

	MIDDLEWARE_CLASSES = [
	    ...
	    'image_moderator.middleware.ImageModeratorMiddleware',
	]

Add the following urlpattern to your root urls.py file::

	urlpatterns = [
	    ...
	    url(r'^image_moderator/', include('image_moderator.urls'))
	]

Example
=======

In your App's models.py, specify image field as *ImageModeratorField()* instead of *models.ImageField()*::

	from image_moderator.models import ImageModeratorField

	class MyModel(models.Model):
	    image = ImageModeratorField(upload_to="assets/", blank=True, null=True)


Now you can call the image API:

| **Syntax:** http://YOUR_DOMAIN_URL/image_moderator/IMAGE_PATH/?size=WIDTHxHEIGHT&crop=center
| **Eg:** http://example.com/image_moderator/products/product-1.jpg/?size=300x200&crop=center

| **Note:** 'size' and 'crop' are optional parameters. If both are not specified, then the actual size of the image will be rendered.
