from django.shortcuts import render
from django.views import View

from .forms import PlaceForm


class HomePageView(View):
    def get(self, request):
        form = PlaceForm()
        return render(request, 'home_page.html', {'form': form})


def search(request):
    return render(request, 'search.html')


def search_results(request):
    place = request.POST['place']
    visit_from = request.POST['visit_from']
    visit_to = request.POST['visit_to']
    climate = request.POST['climate']
    activities = request.POST['activities']
    children_friendly = request.POST['children_friendly']
    scenery = request.POST['scenery']
    continent = request.POST['continent']
    long_stay = request.POST['long_stay']
    short_stay = request.POST['short_stay']
    places_list = []
    if places_list:
        return render(request, 'search_results.html', {'places_list': places_list})
    else:
        return render(request, 'search_failed.html')

