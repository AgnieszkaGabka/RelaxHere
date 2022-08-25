from django.shortcuts import render
from django.views import View


class HomePageView(View):
    def get(self, request):
        form = ToRentForm()
        return render(request, 'home_page.html', {'form': form})


def search(request):
    return render(request, 'search.html')

