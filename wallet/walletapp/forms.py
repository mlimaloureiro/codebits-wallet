from django import forms
from django.contrib.auth.models import User


class UserForm(forms.Form):
    email = forms.CharField(required=True)
    wallet_key = forms.CharField(required=False)
    current = forms.CharField(required=False)
    passwd_new = forms.CharField(required=False)
    passwd_confirmation = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        if kwargs.get('instance', None):
            kwargs.pop('instance')
        return super(UserForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        return cleaned_data
