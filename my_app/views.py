import requests
from requests.compat import quote_plus
from django.shortcuts import render
from bs4 import BeautifulSoup


BASE_CRAIGSLIST_URL = 'https://delhi.craigslist.org/search/hhh?query={}'
# Create your views here.
def home(request):
    return render(request, 'base.html')

def new_search(request):
    search = request.POST.get('search')
    stuff_for_frontend = {
        'search': search,
    }
    return render(request, 'my_app/new_search.html', stuff_for_frontend)