from django import forms

from .models import Place, CLIMATE, ACTIVITY, CHILDREN_ACTIVITY, SCENERY, CONTINENT


class PlaceForm(forms.Form):
    visit_from = forms.DateField(required=False)
    visit_to = forms.DateField(required=False)
    climate = forms.MultipleChoiceField(choices=CLIMATE, widget=forms.SelectMultiple(), required=False)
    activities = forms.MultipleChoiceField(choices=ACTIVITY, widget=forms.SelectMultiple(), required=False)
    children_friendly = forms.MultipleChoiceField(choices=CHILDREN_ACTIVITY, widget=forms.SelectMultiple(), required=False)
    scenery = forms.MultipleChoiceField(choices=SCENERY, widget=forms.SelectMultiple(), required=False)
    continent = forms.MultipleChoiceField(choices=CONTINENT, widget=forms.SelectMultiple(), required=False)
    long_stay = forms.BooleanField(required=False)
    short_stay = forms.BooleanField(required=False)

