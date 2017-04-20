from django.shortcuts import render
from main.models import Stock

# Create your views here.
def stock_akvadar(request):
    stock = Stock.objects.filter(id=2)
    context = {
        'stock': stock,
    }
    return render(request, 'akvadar.html', context=context)