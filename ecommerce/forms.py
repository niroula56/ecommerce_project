from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserForm(UserCreationForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ["email", "password", "username"]