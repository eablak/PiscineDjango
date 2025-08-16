from django.urls import path
from . import views

urlpatterns = [
    path("articles", views.ArticleView.as_view()),
    path("", views.HomeView.as_view(), name="home"),
    path("login", views.LoginView.as_view(), name="login"),
    path("publications", views.PublicationsView.as_view()),
    path("detail/<int:pk>/", views.DetailView.as_view(), name="article_detail"),
]
