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
        if form.data['place']:
            place = request.POST['place']
        if form.data['visit_from']:
            visit_from = request.POST['visit_from']
        if form.data['visit_to']:
            visit_to = request.POST['visit_to']
        if form.data['climate']:
            climate = request.POST['climate']
        if form.data['activities']:
            activities = request.POST['activities']
        if form.data['children_friendly']:
            children_friendly = request.POST['children_friendly']
        if form.data['scenery']:
            scenery = request.POST['scenery']
        if form.data['continent']:
            continent = request.POST['continent']
        if form.data['long_stay']:
            long_stay = request.POST['long_stay']
        if form.data['short_stay']:
            short_stay = request.POST['short_stay']
        if places_list:
            return render(request, 'search_results.html', {'places_list': places_list})
        else:
            return render(request, 'search_failed.html')

