# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20161021_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
