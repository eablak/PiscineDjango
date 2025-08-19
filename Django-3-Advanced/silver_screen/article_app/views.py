from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import logout
from .forms import UserRegisterForm, ArticleForm
from django.db import IntegrityError
# Create your views here.

class ArticleView(generic.ListView):
    
    model = Article
    template_name = "article_app/article_list.html"
    ordering = ['-created']


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
    
class RegisterView(SuccessMessageMixin, generic.CreateView):
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("home")

    template_name = "registiration/register.html"
    success_url = reverse_lazy("home")
    form_class = UserRegisterForm
    success_message = "Registiration is successfull!"


class PublishView(generic.CreateView):
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("home")
        
    template_name = "article_app/publish.html"
    success_url = reverse_lazy("articles")
    form_class = ArticleForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class AddToFavouriteView(generic.CreateView):

    model = UserFavouriteArticle
    success_url = reverse_lazy("favourites")
    fields = []
    template_name = "article_app/favourites.html"

    def form_valid(self, form):
        article_id = self.request.POST.get("article_id")
        article = get_object_or_404(Article, pk=article_id)
        obj, created = UserFavouriteArticle.objects.get_or_create(article=article, user=self.request.user)
        return HttpResponseRedirect(self.success_url)
