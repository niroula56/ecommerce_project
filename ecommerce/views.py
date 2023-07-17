from django.shortcuts import render, get_object_or_404
from .forms import UserForm
from django.views import View
from .models import Product
from django.db.models import Count

# Create your views here.

def home(request):
	return render(request, "home.html")

def about_us(request):
	return render(request, "includes/about_us.html")

def contact(request):
	return render(request, "includes/contact.html")

class CategoryView(View):
	def get(self, request, val):
		product = Product.objects.filter(category=val)
		title = Product.objects.filter(category=val).values('title')
		return render(request, "includes/category.html", locals())


class CategoryTitle(View):
	def get(self, request, val):
		product = Product.objects.filter(title=val)
		title = Product.objects.filter(category=product[0].category).values('title')
		return render(request, "includes/category.html", locals())



def product_detail(request, pk):
	product = get_object_or_404(Product, pk=pk)
	context = {
		"product": product,
	}
	return render(request, "includes/product_detail.html", context=context)

