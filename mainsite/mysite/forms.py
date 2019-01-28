
from django import forms


class PaymentForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your Name'}))
	email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'example@gmail.com'}))
	donation = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
