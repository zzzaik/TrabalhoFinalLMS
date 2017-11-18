# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 19:43
from __future__ import unicode_literals

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nome', models.CharField(blank=True, max_length=100, verbose_name='Nome')),
                ('ra', models.IntegerField(unique=True, verbose_name='RA')),
                ('password', models.CharField(max_length=150)),
                ('user_type', models.CharField(default='C', max_length=1, verbose_name='Tipo de usuário')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', core.models.UsuarioManager()),
            ],
        ),
    ]