from django import forms

from .models import Place


class PlaceForm(forms.ModelForm):

    class Meta:
        model = Place
        fields = ("name", "visit_from", "visit_to", "climate", "activities", "children_friendly", "scenery", "continent",
              "long_stay", "short_stay")

