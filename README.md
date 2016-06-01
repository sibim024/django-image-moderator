#Requirements
<B>django_imagemoderator requires the following:</B>

Python 2.7<br>
Django 1.8+

#Installation
<B>Install package dependency:</B>

```sudo apt-get install libjpeg-dev```<br>
```sudo apt-get install libjpeg8-dev```<br>
```pip install sorl-thumbnail```<br>
```pip install Pillow```

<b>Add 'sorl.thumbnail', 'image_moderator' to your INSTALLED_APPS setting:</b>

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

#Example

In your App's models.py, specify image field as <b>ImageModeratorField()</b> instead of <b>models.ImageField()</b>:

```from image_moderator.models import ImageModeratorField```<br><br>

```class MyModel(models.Model):```</br>
```    image = ImageModeratorField(upload_to=upload_handler, blank=True, null=True)```


Now you can call the image API:

http://YOUR_DOMAIN_URL/image_moderator/IMAGE_NAME.jpg/WIDTHxHEIGHT
<b>Eg:</b> http://example.com/image_moderator/image.jpg/100x100
