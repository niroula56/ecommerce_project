from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'discounted_price', 'category', 'product_image']

admin.site.register(Product, ProductAdmin)