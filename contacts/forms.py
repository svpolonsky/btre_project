from django import forms
from captcha.fields import CaptchaField
from .models import ContactOwner

class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = ContactOwner
        fields = ['name', 'email', 'phone', 'message']

