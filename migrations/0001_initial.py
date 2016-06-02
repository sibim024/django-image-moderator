# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModerator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img_path', models.CharField(max_length=200, null=True, verbose_name=b'Image path')),
                ('app_label', models.CharField(max_length=50, null=True)),
                ('model', models.CharField(max_length=50, null=True)),
                ('approve_status', models.BooleanField(default=False, verbose_name=b'Image status')),
                ('modified_on', models.DateTimeField(auto_now=True, null=True)),
                ('modified_by', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'image_moderator',
                'verbose_name': 'image',
                'verbose_name_plural': 'images',
            },
        ),
    ]
