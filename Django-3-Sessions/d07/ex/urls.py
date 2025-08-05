from django.urls import path
from .views import homepage, register

urlpatterns = [
    path("", homepage.homepage, name="homepage"),
    path("username_ajax/", homepage.getUserName),
    path("register", register.register, name="register"),
    path("login", register.login_page, name="login"),
    path("logout", register.logout_page, name="logout"),
]
