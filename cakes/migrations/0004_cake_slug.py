# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-21 06:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakes', '0003_auto_20170619_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='cake',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
