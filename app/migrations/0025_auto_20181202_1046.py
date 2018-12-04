# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-12-02 10:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_datasource_isecspedit'),
    ]

    operations = [
        migrations.CreateModel(
            name='ValueEd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valueEd', models.CharField(max_length=255, verbose_name='\u0415\u0434\u0438\u043d\u0438\u0446\u044b \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f')),
            ],
            options={
                'verbose_name': '\u0415\u0434\u0438\u043d\u0438\u0446\u044b \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f',
                'verbose_name_plural': '\u0415\u0434\u0438\u043d\u0438\u0446\u044b \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f',
            },
        ),
        # migrations.AddField(
        #     model_name='metering',
        #     name='valueEd',
        #     field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.ValueEd', verbose_name='\u0415\u0434\u0438\u043d\u0438\u0446\u044b \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f'),
        #     preserve_default=False,
        # ),
    ]