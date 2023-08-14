from django.shortcuts import render, redirect
from .forms import CustomerRegistrationForm, LoginForm
from django.contrib import messages


# Create your views here.

def registration(request):
	if request.method == "POST":
		form = CustomerRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Congratulations! User Registration Successfull.")
			return redirect("registration")
		else:
			messages.error(request, "Invalid Input Data.")
		


	else:
		form = CustomerRegistrationForm()
	context = {
	"form": form,
	}
	return render(request, "accounts/registration.html", context=context)
