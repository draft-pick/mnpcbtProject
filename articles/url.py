from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='articles'),
    path('articles/<int:articles_id>/', view_articles, name="view_articles"),
]
