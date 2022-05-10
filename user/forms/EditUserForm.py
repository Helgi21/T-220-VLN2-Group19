from django import forms
from django.contrib.auth import get_user_model
from django.core.validators import EmailValidator

User = get_user_model()


class EditUserForm(forms.Form):
    def __init__(self, username, *args, **kwargs):
        self.username = username
        super(EditUserForm, self).__init__(*args, **kwargs)

    first_name = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=254, label='email', required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}),
                             validators=[EmailValidator])
    profile_picture = forms.URLField(required=False, max_length=999,
                                     widget=forms.URLInput(attrs={'class': 'form-control'}))
    bio = forms.CharField(max_length=255, required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))
    birthday = forms.DateField(required=False, input_formats=['%Y-%m-%d'],
                               widget=forms.DateInput(attrs={'class': 'form-control'}, format='%Y-%m-%d'))

    def clean(self):
        c = super().clean()
        try:
            email = c['email']
        except KeyError:
            return
        new = User.objects.filter(email=email)
        if new.count():
            if new[0].username != self.username:
                raise forms.ValidationError({'email': "A user with this email already exist"})

