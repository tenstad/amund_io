# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-12 18:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abouts', '0002_auto_20170912_1950'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='experience',
            options={'ordering': ['start_year']},
        ),
    ]