from django.shortcuts import render
from .models import *


def index(request):
    context = {
        'title': 'Школа пациента'
    }
    return render(request, 'patients-school/index.html', context=context)


def stay_home(request):
    context = {
        'title': 'Рекомендуемый режим дня больного туберкулезом без бактериовыделения, получающего лечение на дому в условиях режима "Сиди дома"'
    }
    return render(request, 'patients-school/stay-home.html', context=context)
