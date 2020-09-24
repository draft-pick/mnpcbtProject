from django.shortcuts import render
from .models import *


def stay_home(request):
    context = {
        'title': 'Рекомендуемый режим дня больного туберкулезом без бактериовыделения, получающего лечение на дому в условиях режима "Сиди дома"'
    }
    return render(request, 'patients-school/stay-home.html', context=context)