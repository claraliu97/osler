# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-08-17 03:20
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pttrack', '0005_simplehistory_add_change_reason'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('written_datetime', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('clindate', models.DateField(verbose_name=b'Appointment Date')),
                ('clintime', models.TimeField(default=datetime.datetime(2018, 8, 17, 9, 0, tzinfo=utc), verbose_name=b'Time of Appointment')),
                ('appointment_type', models.CharField(choices=[(b'PSYCH_NIGHT', b'Psych Night'), (b'ACUTE_FOLLOWUP', b'Acute Followup'), (b'CHRONIC_CARE', b'Chronic Care')], default=b'CHRONIC_CARE', max_length=15, verbose_name=b'Appointment Type')),
                ('comment', models.TextField(help_text=b'What should happen at this appointment?')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pttrack.Provider')),
                ('author_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pttrack.ProviderType')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pttrack.Patient')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HistoricalAppointment',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('written_datetime', models.DateTimeField(blank=True, editable=False)),
                ('last_modified', models.DateTimeField(blank=True, editable=False)),
                ('clindate', models.DateField(verbose_name=b'Appointment Date')),
                ('clintime', models.TimeField(default=datetime.datetime(2018, 8, 17, 9, 0, tzinfo=utc), verbose_name=b'Time of Appointment')),
                ('appointment_type', models.CharField(choices=[(b'PSYCH_NIGHT', b'Psych Night'), (b'ACUTE_FOLLOWUP', b'Acute Followup'), (b'CHRONIC_CARE', b'Chronic Care')], default=b'CHRONIC_CARE', max_length=15, verbose_name=b'Appointment Type')),
                ('comment', models.TextField(help_text=b'What should happen at this appointment?')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('author', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pttrack.Provider')),
                ('author_type', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pttrack.ProviderType')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='pttrack.Patient')),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical appointment',
            },
        ),
    ]
