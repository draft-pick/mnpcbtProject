from django.db import models
from django.urls import reverse


class Service(models.Model):
    number = models.CharField(max_length=50, verbose_name='Номер')
    code = models.CharField(max_length=100, verbose_name='Код')
    name = models.CharField(max_length=400, verbose_name='Наименование')
    price = models.CharField(max_length=50, verbose_name='Цена')

