from django.shortcuts import render
from django.views import View


class HomePageView(View):
    def get(self, request):
        form = ToRentForm()
        return render(request, 'home_page.html', {'form': form})


def search(request):
    return render(request, 'search.html')


def search_results(request):
    place = request.POST['place']
    items_list = []
    try:
        area = Area.objects.get(city=city)
    except Area.DoesNotExist:
        return render(request, 'search.html')
    items = ToRent.objects.filter(area=area)
    for item in items:
        if item.is_available:
            items_list.append(item)
    return render(request, 'search_results.html', {'items_list': items_list})

