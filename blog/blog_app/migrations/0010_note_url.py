# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-02 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0009_auto_20160102_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='url',
            field=models.URLField(default='replace_me', max_length=2000),
        ),
    ]
