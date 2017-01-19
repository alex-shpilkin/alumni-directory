# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-18 07:16
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20170115_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authcode',
            name='code',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^[^\\s]+$')]),
        ),
        migrations.AlterField(
            model_name='authcode',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='\u0414\u0430\u0442\u0430 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f \u0434\u0430\u043d\u043d\u044b\u0445'),
        ),
        migrations.AlterField(
            model_name='fieldvalue',
            name='status_update_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f \u0441\u0442\u0430\u0442\u0443\u0441\u0430'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='author_code',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='core.AuthCode', verbose_name='\u041a\u043e\u0434 \u0430\u0432\u0442\u043e\u0440\u0430 \u0433\u043e\u043b\u043e\u0441\u0430'),
        ),
    ]