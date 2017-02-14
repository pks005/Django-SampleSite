from django import forms
from django.conf import settings

from newsletter.models import SignUp
from django.core.mail import send_mail


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['email', 'username']

    # Validating email
    def validating_Email(self):
        em = self.cleaned_data.get('email')
        email_base, provider = em.split('@')
        domain, extension = em.split('.')
        if extension != 'com' in em:
            raise forms.ValidationError('Only .com extension is allowed')
        return em


class ContactUsForm(forms.Form):
    full_Name = forms.CharField()
    email = forms.CharField()
    mobileNumber = forms.CharField()
    subject = forms.CharField()
    message = forms.CharField()

