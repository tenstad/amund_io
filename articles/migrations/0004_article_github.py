# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-15 08:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_hidden'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='github',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
