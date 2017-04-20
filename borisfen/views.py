from django.shortcuts import render

from main.models import Stock

# Create your views here.
def stock_borisfen(request):
    stock = Stock.objects.filter(id=1)
    context = {
        'stock': stock,
    }
    return render(request, 'borisfen.html', context=context)
