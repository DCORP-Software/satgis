# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-05 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_metering_valueed'),
    ]

    operations = [
        migrations.AddField(
            model_name='waterobject',
            name='geojson',
            field=models.FileField(default='', upload_to=b''),
            preserve_default=False,
        ),
    ]
