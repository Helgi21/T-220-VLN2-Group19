from django.forms import ModelForm, widgets, Form
from django import forms
from auction.models import Auction, Location, Category
from user.models import User


class AddAuctionForm(Form):
    # TODO: remove user choice, should be automatic the user that is logged in to
    user = forms.ModelChoiceField(queryset=User.objects.all())
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    loc = forms.ModelChoiceField(queryset=Location.objects.all())
    cat = forms.ModelChoiceField(queryset=Category.objects.all())

    image = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    tag = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
