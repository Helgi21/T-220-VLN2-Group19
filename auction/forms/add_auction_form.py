from django.forms import ModelForm, widgets, Form
from django import forms
from auction.models import Auction, Location, Category, Condition
from user.models import User


class AddAuctionForm(Form):
    title = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(max_length=255, required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))
    price = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    image = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    loc = forms.ModelChoiceField(required=True, queryset=Location.objects.all())
    cat = forms.ModelChoiceField(required=True, queryset=Category.objects.all())
    condition = forms.ModelChoiceField(required=True, queryset=Condition.objects.all())
