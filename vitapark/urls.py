"""vitapark URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from main.views import hotel
from akvadar.views import paidservices
from borisfen.views import stock_borisfen

urlpatterns = [
    url(r'^$', hotel, name='hotel'),
    url(r'^stock/', include('main.urls'), name='stock'),
    url(r'^feedback/', include('feedback.urls')),
    url(r'^paid/',  paidservices, name='paidservices'),
    url(r'^akvadar/', include('akvadar.urls')),
    url(r'^borisfen/', stock_borisfen, name='borisfen'),
    url(r'^admin/', admin.site.urls),
]
