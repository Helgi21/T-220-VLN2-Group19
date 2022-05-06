from django.contrib.auth import get_user_model
from django import forms
from django.core.validators import EmailValidator

User = get_user_model()


class EditUserForm(forms.Form):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='email', required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    profile_picture = forms.CharField(required=False, max_length=999,
                                      widget=forms.TextInput(attrs={'class': 'form-control'}),
                                      validators=[EmailValidator])
    birthday = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'form-control'}))
