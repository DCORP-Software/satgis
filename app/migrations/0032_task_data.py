# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-09 10:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_auto_20190609_0956'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='data',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.RasterData', verbose_name='\u0414\u0430\u043d\u043d\u044b\u0435'),
            preserve_default=False,
        ),
    ]