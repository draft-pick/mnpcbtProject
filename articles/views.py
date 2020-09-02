from django.shortcuts import render
from .models import *


def index(request):
    posts = Posts.objects.all()
    image = GalleryPosts.objects.filter(in_the_title=1)
    context = {
        'posts': posts,
        'image': image,
        'title': 'Наши статьи'
    }
    return render(request, 'articles/index.html', context=context)


def view_articles(request, articles_id):
    articles_item = Posts.objects.get(pk=articles_id)
    image_title = GalleryPosts.objects.all().filter(in_the_title=1, product_id=articles_id)
    image = GalleryPosts.objects.all().filter(product_id=articles_id)
    return render(request, 'articles/view_articles.html', {"articles_item": articles_item, 'image': image, 'image_title': image_title})


