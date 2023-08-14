from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm
from django.contrib.auth.models import User


class CustomerRegistrationForm(UserCreationForm):
	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"autofocus": "True", "class": "form-control"}))
	last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class": "form-control"}))
	email = forms.EmailField(widget=forms.TextInput(attrs={"class": "form-control"}))
	password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class":"form-control"}))
	password2 = forms.CharField(label="Password Confirmation", widget=forms.PasswordInput(attrs={"class":"form-control"}))

	class Meta:
		model = User
		fields = ("first_name", "last_name", "email", "username", "password1", "password2")
		widgets = {
			"username": forms.TextInput(attrs={"class": "form-control"}),
		}

class LoginForm(AuthenticationForm):
	username = UsernameField(widget=forms.TextInput(attrs={"class": "form-control", "autofocus": "True"}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))

class MyPasswordResetForm(PasswordChangeForm):
	pass

