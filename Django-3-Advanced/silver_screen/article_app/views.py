from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from .models import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
# Create your views here.

class ArticleView(generic.ListView):
    
    model = Article
    template_name = "article_app/article_list.html"


class HomeView(generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return "/articles"
    

class LoginView(LoginView):
    redirect_authenticated_user = True
    template_name = "registiration/login.html"

    def get_success_url(self):
        return reverse_lazy("home")
    
    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))
    

class PublicationsView(LoginRequiredMixin, generic.ListView):

    model = Article
    template_name = "article_app/publications.html"

    def get_queryset(self):
        return Article.objects.filter(
            author=self.request.user
        ).order_by('created')
    

class DetailView(generic.DetailView):
    model = Article
    template_name = "detail/detail.html"


class LogoutView(LogoutView):
    def get(self, request):
        logout(request)


class FavouritesView(LoginRequiredMixin, generic.ListView):

    model = UserFavouriteArticle
    template_name = "article_app/favourites.html"
    context_object_name = "favourites"

    def get_queryset(self):
        return UserFavouriteArticle.objects.filter(
            user=self.request.user
        ).order_by('article__created')