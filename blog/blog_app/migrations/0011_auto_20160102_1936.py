# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-02 19:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0010_note_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ('-pub_date',)},
        ),
        migrations.AlterField(
            model_name='note',
            name='url',
            field=models.CharField(blank=True, default=None, max_length=2000),
        ),
    ]
