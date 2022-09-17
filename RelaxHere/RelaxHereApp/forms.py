from datetime import datetime

from django import forms

from .models import CLIMATE, ACTIVITY, CHILDREN_ACTIVITY, SCENERY, CONTINENT


class PlaceForm(forms.Form):
    visit_from = forms.DateField(required=False, initial=datetime.now)
    visit_to = forms.DateField(required=False, initial=datetime.now)
    climate = forms.MultipleChoiceField(choices=CLIMATE, widget=forms.SelectMultiple(), required=False,
                                        initial=CLIMATE[0])
    activities = forms.MultipleChoiceField(choices=ACTIVITY, widget=forms.SelectMultiple(), required=False,
                                           initial=ACTIVITY[0])
    children_friendly = forms.MultipleChoiceField(choices=CHILDREN_ACTIVITY, widget=forms.SelectMultiple(),
                                                  required=False, initial=CHILDREN_ACTIVITY[0])
    scenery = forms.MultipleChoiceField(choices=SCENERY, widget=forms.SelectMultiple(), required=False,
                                        initial=SCENERY[0])
    continent = forms.MultipleChoiceField(choices=CONTINENT, widget=forms.SelectMultiple(), required=False,
                                          initial=CONTINENT[0])
    long_stay = forms.BooleanField(required=False)
    short_stay = forms.BooleanField(required=False)

