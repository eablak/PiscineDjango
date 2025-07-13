from django.urls import path
from . import views

urlpatterns = [
    path("ex02/init", views.init),
    path("ex02/populate", views.populate),
    path("ex02/display", views.display)
]
