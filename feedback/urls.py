from django.conf.urls import url, include
from feedback.views import detail

urlpatterns = [
    url(r'^feedback/', detail, name='feedback'),
]
