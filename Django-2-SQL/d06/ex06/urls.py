from django.urls import path
from . import views

urlpatterns = [
    path("ex06/init", views.init),
    path("ex06/populate", views.populate),
    path("ex06/display", views.display),
    path("ex06/update", views.update),
]
