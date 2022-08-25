from django import forms

from RelaxHere.RelaxHereApp.models import Place


class PlaceForm(forms.Form):

    model = Place
    fields = ("name", "visit_from", "visit_to", "climate", "activities", "children_frinedly", "scenery", "continent", "long_stay", "short_stay")

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('')
        super(PlaceForm, self).__init__(*args, **kwargs)
