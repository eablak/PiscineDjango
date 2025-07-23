from django.urls import path
from . import views

urlpatterns = [
    path("ex04/init", views.init),
    path("ex04/populate", views.populate),
    path("ex04/display", views.display),
    path("ex04/remove", views.remove)
]
