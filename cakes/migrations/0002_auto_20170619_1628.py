# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cake',
            name='description',
            field=models.TextField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='cake',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
