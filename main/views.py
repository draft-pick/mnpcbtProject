from django.shortcuts import render
from django.http import HttpResponse
from structure.models import Branches


def index(request):
    branches = Branches.objects.all()
    context = {
        'branches': branches,
        'title': 'Главная страница',
    }
    return render(request, 'main/index.html', context=context)


def management(request):
    context = {
        'title': 'Руководство Центра'
    }
    return render(request, 'main/management.html', context=context)


def chief_page(request):
    context = {
        'title': 'Страница главного фтизиатра'
    }
    return render(request, 'main/chief-phthisiatricians-page.html', context=context)


