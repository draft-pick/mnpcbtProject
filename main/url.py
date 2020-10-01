from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('management/', management, name='management'),
    path('chief-phthisiatricians-page/', chief_page, name='chief_page'),
]
