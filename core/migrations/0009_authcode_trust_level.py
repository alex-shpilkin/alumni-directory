# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-07 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20170206_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='authcode',
            name='trust_level',
            field=models.FloatField(default=1, verbose_name='\u0423\u0440\u043e\u0432\u0435\u043d\u044c \u0434\u043e\u0432\u0435\u0440\u0438\u044f'),
        ),
    ]