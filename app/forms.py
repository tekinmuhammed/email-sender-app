# email_sender/forms.py
from django import forms
from .models import Email

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['to_email', 'subject', 'message']
