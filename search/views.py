from typing import NamedTuple
from django.shortcuts import render, HttpResponse
from search.models import Products

# Create your views here.


def index(request):
    return render(request, "index.html")

def search(request):
    query = request.GET['search']
    product = Products.objects.filter(name__icontains=query)
    param = {"product" : product}

    return render(request, "search.html", param )