from django.urls import path
from . import views

urlpatterns = [
    path("", views.LoginView.as_view(), name="account"),
    path("login_check", views.LoginCheckView.as_view(), name="login_check"),
    path("logout_view", views.LogoutView.as_view(), name="logout_view")
]