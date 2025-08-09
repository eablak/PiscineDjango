from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import TipModel
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(UserCreationForm):
    class Meta:
    
        model = User
        fields = ["username", "password1", "password2"]
        labels = {
            "username": "Username",
            "password1": "Password",
            "password2": "Password (again)",
        }
        help_texts = {
            "username": "",
            "password1": "",
            "password2": "",
        }


class TipModelForm(forms.ModelForm):
    class Meta:
        model = TipModel
        fields = ["content"]