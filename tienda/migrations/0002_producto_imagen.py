# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-07 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.FileField(blank=True, null=True, upload_to='tienda/%Y/%m/%d/'),
        ),
    ]
