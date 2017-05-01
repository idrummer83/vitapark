
from django.conf.urls import url
from akvadar.views import stockakvadar, healthcenter

urlpatterns = [
    url(r'^$', stockakvadar, name='akvadar'),
    url(r'^(?P<context>[0-9]+)$', healthcenter, name='likuvalna-baza'),
    # url(r'1', healthcenter, name='likuvalna-baza'),
    # url(r'^(?P<hs_id>\+d)$', ),
]
