from django.urls import path
from . import views

# create views for urls

urlpatterns = [
    path("ex00/", views.index),
]
