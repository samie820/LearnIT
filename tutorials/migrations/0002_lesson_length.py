# -*- coding: utf-8 -*-
# Generated by Django 1.11rc1 on 2017-10-15 18:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='length',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
