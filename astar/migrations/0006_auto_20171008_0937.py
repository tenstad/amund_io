# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-08 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astar', '0005_tileconfig_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tileconfig',
            name='title',
            field=models.CharField(default='Config', max_length=50),
        ),
    ]
