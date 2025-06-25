from django.urls import path
from . import views

urlpatterns = [
    path("ex01/django", views.django),
    path("ex01/display", views.display),
    path("ex01/templates", views.templates),
]
