# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_moderator', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagemoderator',
            options={'verbose_name': 'image', 'verbose_name_plural': 'images'},
        ),
        migrations.AlterField(
            model_name='imagemoderator',
            name='approve_status',
            field=models.BooleanField(default=False, verbose_name=b'Image status'),
        ),
    ]
