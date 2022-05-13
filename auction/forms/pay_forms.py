from auction import models
from user import models as user_models
from django import forms


class ContactPayForm(forms.Form):
    first_name = forms.CharField(required=True, max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=True, max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    street_name = forms.CharField(required=True, max_length=255,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    house_number = forms.IntegerField(required=True, min_value=0, max_value=9999,
                                      widget=forms.NumberInput(attrs={'class': 'form-control'}))
    city = forms.CharField(required=True, max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    country = forms.ModelChoiceField(required=True, queryset=user_models.Country.objects.all())
    zip = forms.CharField(required=True, max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))


class PaymentPayForm(forms.Form):
    cardholder_first_name = forms.CharField(required=True, max_length=150, label="Cardholders First Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
    cardholder_last_name = forms.CharField(required=True, max_length=150, label="Cardholders Last Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
    card_number = forms.IntegerField(required=True, min_value=1000000000000000, max_value=9999999999999999,
                                     widget=forms.NumberInput(attrs={'class': 'form-control'}))
    expires = forms.DateField(required=False, input_formats=['%Y-%m'], label='Expiry date - (YYYY-MM)',
                              widget=forms.DateInput(attrs={'class': 'form-control'}, format='%Y-%m'))
    cvc = forms.IntegerField(required=True, min_value=100, max_value=999,
                             widget=forms.DateInput(attrs={'class': 'form-control'}))