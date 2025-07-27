from django import forms

class InputForm(forms.Form):
    textfield = forms.CharField(max_length=200)