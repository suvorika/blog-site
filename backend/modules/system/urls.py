from django.urls import path

from .views import (
    ProfileUpdateView,
    ProfileDetailView,
    UserRegisterView,
    UserLoginView,
    UserPasswordChangeView,
)

urlpatterns = [
    path("user/edit/", ProfileUpdateView.as_view(), name="profile_edit"),
    path("user/<str:slug>/", ProfileDetailView.as_view(), name="profile_detail"),
    path("register/", UserRegisterView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("password-change/", UserPasswordChangeView.as_view(), name="password_change"),
]
