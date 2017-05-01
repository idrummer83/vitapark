from django.conf.urls import url, include
from django.contrib import admin
from main.views import hotel, stock

urlpatterns = [
    # url(r'^$', hotel, name='hotel'),
    # url(r'^feedback/', feedback, name='feedback'),
    url(r'^stockall/', stock, name='stock'),

    # url(r'^borisfen/', stock_borisfen, name='borisfen'),

]
