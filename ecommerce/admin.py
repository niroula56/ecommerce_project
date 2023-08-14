from django.contrib import admin
from .models import Product, Customer

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'discounted_price', 'category', 'product_image']

admin.site.register(Product, ProductAdmin)


class CustomerAdmin(admin.ModelAdmin):
	list_display = ['id', 'user', 'locality', 'city', 'state', 'zipcode']
admin.site.register(Customer, CustomerAdmin)