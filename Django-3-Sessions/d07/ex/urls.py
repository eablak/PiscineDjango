from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage),
    path("username_ajax/", views.getUserName),
    path("register", views.register, name="register"),
]
