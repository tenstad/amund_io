# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 22:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20170819_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(blank=True, max_length=4000),
        ),
        migrations.AlterField(
            model_name='article',
            name='ingress',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]