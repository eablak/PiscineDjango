from django.urls import path
from . import views

urlpatterns = [
    path("articles", views.ArticleView.as_view(), name="articles"),
    path("", views.HomeView.as_view(), name="home"),
    path("login", views.LoginView.as_view(), name="login"),
    path("publications", views.PublicationsView.as_view(), name="publications"),
    path("detail/<int:pk>/", views.DetailView.as_view(), name="article_detail"),
    path("logout", views.LogoutView.as_view(), name="logout"),
    path("favourites", views.FavouritesView.as_view(), name="favourites"),
    path("register", views.RegisterView.as_view(), name="register"),
    path("publish", views.PublishView.as_view()),
    path("add_to_favourite", views.AddToFavouriteView.as_view(), name="add_to_favourite"),

]
