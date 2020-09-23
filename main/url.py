from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('existing_organizations/', existing_org, name='existing_org'),
]
