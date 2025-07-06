from django import forms

class InputForm(forms.Form):
    context = forms.CharField(widget=forms.Textarea())