from django import forms


class MakeOfferForm(forms.Form):
    price = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))