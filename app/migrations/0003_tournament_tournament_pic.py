# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-14 22:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190714_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='tournament_pic',
            field=models.ImageField(blank=True, upload_to='quest_pics/'),
        ),
    ]
