# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 08:52
from __future__ import unicode_literals

from django.db import migrations, models
import mains.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SlideImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=mains.models.upload_location)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
