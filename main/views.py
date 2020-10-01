from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


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
