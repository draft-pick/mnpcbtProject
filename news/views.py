from django.shortcuts import render
from .models import *


def index(request):
    news = News.objects.all()
    image = GalleryNews.objects.filter(in_the_title=1)
    context = {
        'news': news,
        'image': image,
        'title': 'Наши новости',
    }
    return render(request, 'news/index.html', context=context)
