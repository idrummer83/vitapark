from django.shortcuts import render
from .models import Hotel, Stock

# Create your views here.
from django.http.response import HttpResponse
from django.shortcuts import render

def hotel(request):
    hotel = Hotel.objects.all()
    stock = Stock.objects.filter(stock_both=True)
    context = {
        'hotel': hotel,
        'stock': stock,
    }
    return render(request, 'index.html', context=context)

def stock(request):
    stock = Stock.objects.all()
    context = {
        'stock': stock,
    }
    return render(request, 'stock.html', context=context)
