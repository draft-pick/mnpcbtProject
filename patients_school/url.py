from django.urls import path

from patients_school.views import *

urlpatterns = [
    path('', index, name='patients-school'),
    path('1/', stay_home, name='stay_home'),
]
