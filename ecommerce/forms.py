from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Customer


class UserForm(UserCreationForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ["email", "password", "username"]

class CustomerProfileForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = ["name", "locality", "city", "mobile", "state", "zipcode"]
		widgets = {
		"name": forms.TextInput(attrs={"class": "form-control"}),
		"locality": forms.TextInput(attrs={"class": "form-control"}),
		"city": forms.TextInput(attrs={"class": "form-control"}),
		"mobile": forms.NumberInput(attrs={"class": "form-control"}),
		"state": forms.TextInput(attrs={"class": "form-control"}),
		"zipcode": forms.NumberInput(attrs={"class": "form-control"}),
		}
