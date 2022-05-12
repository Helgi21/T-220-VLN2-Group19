from django import forms


class ReviewForm(forms.Form):
    rating = forms.IntegerField(min_value=0, max_value=10, widget=forms.NumberInput)
    review_text = forms.CharField(max_length=255, widget=forms.Textarea)
