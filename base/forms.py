import smtplib
from email import message
from django import forms
from django.core.mail import send_mail

class EmailForm(forms.Form):
  name = forms.CharField(widget=forms.TextInput(attrs={
    "type": "text",
    "class": "form-control",
    "name": "name",
    "id": "name",
    "placeholder": "Your Name",
    "required": True,
  }))
  email = forms.EmailField(widget=forms.EmailInput(attrs={
    "type": "email",
    "class": "form-control",
    "name": "email",
    "id": "email",
    "placeholder": "Your Email",
    "required": True,
  }))
  subject = forms.CharField(widget=forms.TextInput(attrs={
    "type": "text",
    "class": "form-control",
    "name": "subject",
    "id": "subject",
    "placeholder": "Subject",
    "required": True,
  }))
  message = forms.CharField(widget=forms.Textarea(attrs={
    "class": "form-control",
    "name": "message",
    "id": "mesage",
    "rows": 5,
    "placeholder": "Message",
    "required": True,
  }))
