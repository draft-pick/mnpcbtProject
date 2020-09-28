from django.shortcuts import render
from .models import *


def covid_19(request):
    context = {
        'title': 'Специалистам COVID-19'
    }
    return render(request, 'covid_19/index.html', context=context)
