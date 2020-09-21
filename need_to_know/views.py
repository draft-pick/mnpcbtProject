from django.shortcuts import render
from .models import *


def index(request):
    context = {
        'title': 'Это нужно знать!',
    }
    return render(request, 'need-to-know/index.html', context=context)
