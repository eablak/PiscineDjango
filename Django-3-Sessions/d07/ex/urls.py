from django.urls import path
from .views import homepage, register

urlpatterns = [
    path("", homepage.homepage),
    path("username_ajax/", homepage.getUserName),
    path("register", register.register, name="register"),
]
