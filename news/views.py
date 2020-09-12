from django.shortcuts import render
from .models import *


def index(request):
    context = {
        'title': 'Наши новости',
    }
    return render(request, 'news/index.html', context=context)
