# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-06 13:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170706_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=200),
        ),
    ]
