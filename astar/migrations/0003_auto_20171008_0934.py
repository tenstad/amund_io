# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-08 09:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astar', '0002_board_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='board',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='board',
            name='tile_config',
            field=models.TextField(default='', max_length=300),
        ),
    ]
