# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-15 13:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0014_auto_20181017_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamsubtitlescompleted',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
