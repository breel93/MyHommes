# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-09-15 01:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtor', '0003_auto_20180914_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='realtor',
            name='agree_to_terms',
            field=models.BooleanField(default=False),
        ),
    ]
