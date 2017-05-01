from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from main.models import Stock
from .models import HealthCenter, HealthService, Feedback
from akvadar.forms import Feedbackform
# from vitapark import akvadar

# Create your views here.
def stockakvadar(request):
    stock = Stock.objects.filter(id=1)
    hc = HealthCenter.objects.all()
    # hs = HealthService.objects.all()
    context = {
        'stock': stock,
        'hc': hc,
        # 'hs': hs,
    }
    return render(request, 'akvadar.html', context=context)


def healthcenter(request, context):
    # hc = HealthCenter.objects.filter(pk=context)
    hs = HealthService.objects.all()
    # hs = HealthCenter.objects.filter(link=context)
    # slug = HealthCenter.objects.all()
    context = {
        # 'dfg': context,
        'hs': hs,
        # 'hc': hc,
        # 'slug': slug,
    }
    return render(request, 'asd.html', context=context)
