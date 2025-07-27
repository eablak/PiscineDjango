from django.urls import path
from . import views

urlpatterns = [
    path("ex07/populate", views.populate),
    path("ex07/display", views.display),
    path("ex07/update", views.update),
]
