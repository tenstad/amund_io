# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-08 09:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('astar', '0006_auto_20171008_0937'),
    ]

    operations = [
        migrations.RenameField(
            model_name='board',
            old_name='tile_config',
            new_name='tile_config_fk',
        ),
    ]
