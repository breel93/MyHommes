# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-09-15 23:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtor', '0005_auto_20180915_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='realtor/'),
        ),
    ]
