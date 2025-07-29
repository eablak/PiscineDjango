from django.urls import path
from . import views

urlpatterns = [
    path("ex08/init", views.init),
    path("ex08/populate", views.populate),
]
