from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
# Create your views here.
from django.shortcuts import render

from akvadar.forms import Feedbackform
from .models import Hotel, Stock


def hotel(request):
    context = {
        'hotel': Hotel.objects.all(),
        # 'stock': Stock.objects.filter(stock_both=True),
    }
    return render(request, 'index.html', context=context)


def stock(request):
    stock = Stock.objects.all()
    context = {
        # 'stock': Stock.objects.filter(stock_both=True),
        'stock': stock,
    }
    return render(request, 'stock.html', context=context)
