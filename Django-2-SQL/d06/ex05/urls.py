from django.urls import path
from . import views

urlpatterns = [
    path("ex05/populate", views.populate),
    path("ex05/display", views.display),
    path("ex05/remove", views.remove),
]
