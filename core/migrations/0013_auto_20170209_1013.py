# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-09 10:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20170207_2354'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set([]),
        ),
    ]