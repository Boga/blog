# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-04 12:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0014_auto_20160104_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='note',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='blog_app.Note'),
        ),
        migrations.AlterField(
            model_name='note',
            name='body',
            field=models.TextField(blank=True, db_index=True, max_length=4000),
        ),
    ]
