# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakes', '0007_auto_20170629_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cake',
            name='weight',
            field=models.CharField(choices=[(b'1', b'1'), (b'1.5', b'1.5'), (b'2', b'2'), (b'2.5', b'2.5'), (b'3', b'3'), (b'3.5', b'3.5'), (b'4', b'4'), (b'4.5', b'4.5'), (b'5', b'5')], max_length=5, null=True),
        ),
    ]