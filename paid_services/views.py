from django.shortcuts import render
from .models import *


def index(request):
    context = {
        'title': 'Платные услуги'
    }
    return render(request, 'paid-services/index.html', context=context)
