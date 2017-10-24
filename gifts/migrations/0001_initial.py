# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-11 06:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import gifts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderPillo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_date', models.DateField()),
                ('delivery_time', models.TimeField(null=True)),
                ('quantity', models.IntegerField()),
                ('gift_message', models.TextField(max_length=200)),
                ('phone_number', models.CharField(max_length=15, validators=[gifts.models.phone_validator])),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pillo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('description', models.TextField(max_length=400, null=True)),
                ('price', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to=gifts.models.upload_location)),
                ('view_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='orderpillo',
            name='gift',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pillo', to='gifts.Pillo'),
        ),
        migrations.AddField(
            model_name='orderpillo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='giftorderuser', to=settings.AUTH_USER_MODEL),
        ),
    ]
