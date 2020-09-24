from django.urls import path

from patients_school.views import *

urlpatterns = [
    path('', stay_home, name='stay_home'),
]
