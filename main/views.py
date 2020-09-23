from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def existing_org(request):
    context = {
        'title': 'Вышестоящие организации'
    }
    return render(request, 'main/existing_organizations.html', context=context)
