from urllib import request

from django.shortcuts import render
from django.views import View
from django.db.models import Q
from .forms import PlaceForm
from .models import Place


class HomePageView(View):
    def get(self, request):
        form = PlaceForm()
        return render(request, 'home_page.html', {'form': form})


def search(request):
    return render(request, 'search.html')


class SearchResultsView(View):
    def get(self, request):
        form = PlaceForm()
        return render(request, 'search.html', {'form': form})

    def post(self, request):
        form = PlaceForm(request.POST)
        places_list = []
        factors = []
        if 'place' in request.POST:
            place = request.POST['place']
            places = Place.objects.filter(name=place)
            if places:
                places_list.append(places)
        if 'visit_from' in request.POST:
            visit_from = request.POST['visit_from']
            places = Place.objects.filter(visit_from=visit_from)
            if places:
                places_list.append(places)
        if 'visit_to' in request.POST:
            visit_to = request.POST['visit_to']
            places = Place.objects.filter(visit_to=visit_to)
            if places:
                places_list.append(places)
        if 'climate' in request.POST:
            climate = request.POST['climate']
            places = Place.objects.filter(climate=climate)
            if places:
                places_list.append(places)
        if 'activities' in request.POST:
            activities = request.POST['activities']
            places = Place.objects.filter(activities=activities)
            if places:
                places_list.append(places)
        if 'children_friendly' in request.POST:
            children_friendly = request.POST['children_friendly']
            places = Place.objects.filter(children_friendly=children_friendly)
            if places:
                places_list.append(places)
        if 'scenery' in request.POST:
            scenery = request.POST['scenery']
            places = Place.objects.filter(scenery=scenery)
            if places:
                places_list.append(places)
        if 'continent' in request.POST:
            continent = request.POST['continent']
            places = Place.objects.filter(continent=continent)
            if places:
                places_list.append(places)
        if 'long_stay' in request.POST:
            long_stay = request.POST['long_stay']
            places = Place.objects.filter(long_stay=long_stay)
            if places:
                places_list.append(places)
        if 'short_stay' in request.POST:
            short_stay = request.POST['short_stay']
            places = Place.objects.filter(short_stay=short_stay)
            if places:
                places_list.append(places)
        if places_list:
            return render(request, 'search_results.html', {'places_list': places_list})
        else:
            return render(request, 'search_failed.html')

