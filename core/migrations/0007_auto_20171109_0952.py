# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-09 11:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20171109_0951'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='ative',
            new_name='ativo',
        ),
    ]
