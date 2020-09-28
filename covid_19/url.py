from django.urls import path

from .views import *

urlpatterns = [
    path('', covid_19, name='covid-19'),
]
