# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-19 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_metering'),
    ]

    operations = [
        migrations.AddField(
            model_name='metering',
            name='time',
            field=models.CharField(default='', max_length=255, verbose_name='\u0412\u0440\u0435\u043c\u044f'),
            preserve_default=False,
        ),
    ]
