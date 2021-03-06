# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-11-08 13:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_auto_20181107_0551'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rasterdata',
            options={'verbose_name': '\u0417\u0430\u0433\u0440\u0443\u0436\u0435\u043d\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435', 'verbose_name_plural': '\u0417\u0430\u0433\u0440\u0443\u0436\u0435\u043d\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435'},
        ),
        migrations.AlterModelOptions(
            name='rasterlayer',
            options={'verbose_name': '\u0421\u043b\u043e\u0438 \u0434\u0430\u043d\u043d\u044b\u0445', 'verbose_name_plural': '\u0421\u043b\u043e\u0438 \u0434\u0430\u043d\u043d\u044b\u0445'},
        ),
        migrations.AddField(
            model_name='metering',
            name='lat',
            field=models.CharField(default='', max_length=255, verbose_name='\u0428\u0438\u0440\u043e\u0442\u0430'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='metering',
            name='long',
            field=models.CharField(default='', max_length=255, verbose_name='\u0414\u043e\u043b\u0433\u043e\u0442\u0430'),
            preserve_default=False,
        ),
    ]
