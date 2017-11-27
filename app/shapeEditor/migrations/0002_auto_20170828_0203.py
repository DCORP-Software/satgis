# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 02:03
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shapeEditor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttributeValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, max_length=255, null=True)),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shapeEditor.Attribute')),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom_point', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('geom_multipoint', django.contrib.gis.db.models.fields.MultiPointField(blank=True, null=True, srid=4326)),
                ('geom_multilinestring', django.contrib.gis.db.models.fields.MultiLineStringField(blank=True, null=True, srid=4326)),
                ('geom_multilipolygon', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4326)),
                ('geom_geometrycolletion', django.contrib.gis.db.models.fields.GeometryCollectionField(blank=True, null=True, srid=4326)),
                ('shapefile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shapeEditor.Shapefile')),
            ],
        ),
        migrations.AddField(
            model_name='attributevalue',
            name='feature',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shapeEditor.Feature'),
        ),
    ]