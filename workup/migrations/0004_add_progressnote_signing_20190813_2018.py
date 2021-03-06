# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-14 01:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import pttrack.validators


class Migration(migrations.Migration):

    dependencies = [
        ('pttrack', '0007_referraltype_is_active'),
        ('workup', '0003_historicalworkup_add_attending_validator_20190324_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalprogressnote',
            name='signed_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='historicalprogressnote',
            name='signer',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pttrack.Provider'),
        ),
        migrations.AddField(
            model_name='progressnote',
            name='signed_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='progressnote',
            name='signer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='signed_progress_notes', to='pttrack.Provider', validators=[pttrack.validators.validate_attending]),
        ),
        migrations.AlterField(
            model_name='historicalworkup',
            name='attending',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pttrack.Provider'),
        ),
        migrations.AlterField(
            model_name='historicalworkup',
            name='clinic_day',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='workup.ClinicDate'),
        ),
        migrations.AlterField(
            model_name='historicalworkup',
            name='signer',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pttrack.Provider'),
        ),
        migrations.AlterField(
            model_name='workup',
            name='clinic_day',
            field=models.ForeignKey(help_text=b'When was the patient seen?', on_delete=django.db.models.deletion.CASCADE, to='workup.ClinicDate'),
        ),
    ]
