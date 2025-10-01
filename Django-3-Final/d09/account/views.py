from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):
    
    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        return render(request, "login.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
    
            user = request.user
            username = user.username
            return JsonResponse({"success":"True", "username": username})
        else:
            return JsonResponse({"success":"False"})

class LoginCheckView(View):
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = request.user
            username = user.username
            return JsonResponse({"success":"True", "username":username})
        else:
            return JsonResponse({"success":"False"})

@method_decorator(csrf_exempt, name='dispatch')
class LogoutView(View):
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
            return JsonResponse({"success":"True"})
        return JsonResponse({"success":"False"})

