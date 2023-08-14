from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from accounts.forms import LoginForm, MyPasswordResetForm


urlpatterns = [
	path("registration/", views.registration, name="registration"),
	path("login/", auth_view.LoginView.as_view(template_name="accounts/login.html", authentication_form=LoginForm), name="login"),
    path("password-reset/", auth_view.PasswordResetView.as_view(template_name="accounts/password_reset.html", form_class = MyPasswordResetForm), name="password_reset"),
]