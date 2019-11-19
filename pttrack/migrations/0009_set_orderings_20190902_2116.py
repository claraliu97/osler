# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-09-03 02:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pttrack', '0008_actioninstruction_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actionitem',
            options={'ordering': ['-written_datetime', '-last_modified']},
        ),
        migrations.AlterModelOptions(
            name='document',
            options={'ordering': ['-written_datetime', '-last_modified']},
        ),
        migrations.AlterModelOptions(
            name='ethnicity',
            options={'verbose_name_plural': 'ethnicities'},
        ),
    ]
