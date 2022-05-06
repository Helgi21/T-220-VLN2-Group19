from django import forms


class MakeCounterOfferForm(forms.Form):
    price = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))