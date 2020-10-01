from django.shortcuts import render
from .models import *


def index(request):
    context = {
        'title': 'Отзывы'
    }
    return render(request, 'reviews/index.html', context=context)
