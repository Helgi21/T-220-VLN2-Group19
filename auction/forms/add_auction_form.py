from django.forms import ModelForm, widgets
from django import forms
from auction.models import Auction, Image


class AddAuctionForm(ModelForm):
    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    tag = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Auction
        exclude = {'id'}
        widgets = {
            'title': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'loc': widgets.Select(attrs={'class': 'form-control'}),
            'cat': widgets.Select(attrs={'class': 'form-control'}),
        }


class AddImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['link', 'auction']
