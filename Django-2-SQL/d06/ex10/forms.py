from django import forms
from .models import *

def get_genders():


    gender_data = People.objects.values_list("gender",flat=True).distinct()

    tuple_gender = [(gender,gender) for gender in gender_data]
    return tuple_gender


class InputForm(forms.Form):

    minimumDate_movies = forms.DateField(label="Minimum Date")
    maximumDate_movies = forms.DateField(label="Maximum Date")
    diameter_planet = forms.IntegerField(label="Diameter")

    def __init__(self, *args, **kwargs):
        super(InputForm, self).__init__(*args, **kwargs)

        self.fields['Gender Character'] = forms.ChoiceField(
            choices=get_genders() )