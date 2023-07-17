from django.urls import path
from . import views

urlpatterns = [
	path("", views.home, name="home"),

	path("category/<slug:val>/", views.CategoryView.as_view(), name="category"),
	path("product_detail/<int:pk>/", views.product_detail, name="product_detail"),
	path("product_title/<val>", views.CategoryTitle.as_view(), name="category_title"),
	path("about_us/", views.about_us, name="about_us"),
	path("contact/", views.contact, name="contact"),
]