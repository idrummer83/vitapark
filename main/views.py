from django.shortcuts import render
from .models import Hotel, Stock

# Create your views here.
from django.http.response import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {'qwe': 'aaaa'})

def stock(request):
    site = Stock.objects.all()
    context = {'site': site}
    return render(request, 'index.html', context=context)

