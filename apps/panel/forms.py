from django import forms
from .models import *


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUsModel
        exclude = ['admin_message', 'seen_by_admin']