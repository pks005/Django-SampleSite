# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 09:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='username',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]