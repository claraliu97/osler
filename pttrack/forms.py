from django import forms
from django.forms import ModelForm

from . import models


class PatientForm(ModelForm):
    class Meta:
        model = models.Patient
        exclude = []


class WorkupForm(ModelForm):
    class Meta:
        model = models.Workup
        exclude = ['patient', 'clinic_day', 'author']


class FollowupForm(ModelForm):
    class Meta:
        model = models.Followup
        exclude = ['patient', 'written_date', 'author']