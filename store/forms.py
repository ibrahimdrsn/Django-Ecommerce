from django import forms

class OrderForm(forms.Form):
    fullname = forms.CharField(max_length=100)
    address = forms.CharField(widget=forms.Textarea)
    phone_number = forms.CharField(max_length=20)