# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-07 09:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0017_auto_20160104_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='body_html',
            field=models.TextField(blank=True, max_length=4000),
        ),
    ]
