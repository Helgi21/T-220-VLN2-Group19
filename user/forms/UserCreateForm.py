from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from django.utils.safestring import mark_safe

User = get_user_model()


class UserCreateForm(UserCreationForm, forms.Form):
    email = forms.EmailField(max_length=254, label=mark_safe('Email'), required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")

    def clean(self):
        try:
            email = self.cleaned_data['email'].lower()
        except KeyError:
            return
        new = User.objects.filter(email=email)
        if new.count():
            raise forms.ValidationError("A user with this email already exist")
