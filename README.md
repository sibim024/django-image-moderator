#django_image_moderator

django_image_moderator is useful when there is a need to moderate images uploaded from any model. It recognizes image uploads from any model and provides a provision to approve / reject them from the django-admin backend. It also provides an API to view approved images. Rejected images will not be rendered in the API.

#Requirements
<b>django_imagemoderator requires the following:</b>

Python 2.7<br>
Django 1.8+

#Installation
<b>Install package dependency:</b>

```sudo apt-get install libjpeg-dev```<br>
```sudo apt-get install libjpeg8-dev```<br>
```pip install sorl-thumbnail```<br>
```pip install Pillow```

<b>Add 'sorl.thumbnail', 'image_moderator' to your INSTALLED_APPS setting:</b>

```INSTALLED_APPS = (```<br>
    ```...```<br>
    ```'sorl.thumbnail',```<br>
    ```'image_moderator',```<br>
```)```

<b>Add middleware class to MIDDLEWARE_CLASSES setting:</b>

```MIDDLEWARE_CLASSES = [```<br>
    ```...```<br>
    ```'image_moderator.middleware.ImageModeratorMiddleware',```<br>
```]```

<b>Add the following urlpattern to your root urls.py file:</b>

```urlpatterns = [```<br>
    ```...```<br>
    ```url(r'^', include('image_moderator.urls'))```<br>
```]```

#Example

In your App's models.py, specify image field as <b>ImageModeratorField()</b> instead of <b>models.ImageField()</b>:

```from image_moderator.models import ImageModeratorField```<br>

```class MyModel(models.Model):```</br>
```    image = ImageModeratorField(upload_to=upload_handler, blank=True, null=True)```


Now you can call the image API:

http://YOUR_DOMAIN_URL/image_moderator/IMAGE_NAME.jpg/WIDTHxHEIGHT<br>
<b>Eg:</b> http://example.com/image_moderator/image.jpg/100x100
