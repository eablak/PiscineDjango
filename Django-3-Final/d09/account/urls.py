from django.urls import path
from . import views


urlpatterns = [
    path("account", views.login_view, name="account"),
    path("logout", views.logout_view, name="logout"),
]
