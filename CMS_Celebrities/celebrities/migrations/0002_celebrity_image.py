# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-15 01:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celebrities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='celebrity',
            name='image',
            field=models.FileField(default=2, upload_to=b''),
            preserve_default=False,
        ),
    ]
