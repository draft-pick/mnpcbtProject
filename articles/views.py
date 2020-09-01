from django.shortcuts import render
from .models import *


def index(request):
    posts = Posts.objects.all()
    image = GalleryPosts.objects.all().filter(in_the_title=1)
    context = {
        'posts': posts,
        'image': image,
        'title': 'Список статей'
    }
    return render(request, 'articles/index.html', context=context)
