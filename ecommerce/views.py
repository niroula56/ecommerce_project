from django.shortcuts import render
from .forms import UserForm

# Create your views here.

def home(request):
	form = UserForm()
	context = {
	"form": form,
	}
	return render(request, "base.html", context=context)