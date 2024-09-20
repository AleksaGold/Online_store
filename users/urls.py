from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import UserCreateView, email_verification, EmailConfirmView, UserPasswordResetView, NewPasswordView, \
    EmailNotFoundView

app_name = UsersConfig.name

urlpatterns = [
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", UserCreateView.as_view(), name="register"),
    path("email-confirm/<str:token>/", email_verification, name="email-confirm"),
    path("email-confirm/", EmailConfirmView.as_view(), name="email_confirm"),
    path("password_reset/", UserPasswordResetView.as_view(template_name="password_reset.html"), name="password_reset"),
    path("new_password/", NewPasswordView.as_view(), name="new_password"),
    path("email_not_found/", EmailNotFoundView.as_view(), name="email_not_found"),
]
