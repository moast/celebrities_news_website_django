# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-15 02:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celebrities', '0005_auto_20170815_0541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celebrity',
            name='image',
            field=models.FileField(upload_to='celebrities/'),
        ),
    ]