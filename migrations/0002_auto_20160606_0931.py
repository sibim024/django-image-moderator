# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_moderator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemoderator',
            name='approve_status',
            field=models.BooleanField(default=False, verbose_name=b'Approved'),
        ),
        migrations.AlterField(
            model_name='imagemoderator',
            name='model',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Model'),
        ),
    ]
