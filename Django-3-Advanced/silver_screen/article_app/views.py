from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from .models import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.

class ArticleView(generic.ListView):
    
    model = Article


class HomeView(generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return "/article"
    

class LoginView(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("home")
    
    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))