from django.urls import path
from . import views

urlpatterns = [
    path("article", views.ArticleView.as_view()),
    path("", views.HomeView.as_view(), name="home"),
    path("login", views.LoginView.as_view(), name="login"),
]
