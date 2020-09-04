from django.db import models
from django.urls import reverse
# from ckeditor_uploader.fields import RichTextUploadingField


class Branches(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование')
    address = models.TextField(blank=True, verbose_name='Адрес')
    phones = models.TextField(verbose_name='Телефоны')
    email = models.EmailField(verbose_name='E-mail')
    content = models.TextField(blank=True, verbose_name='Контент')

    def get_absolute_url(self):
        return reverse('view_branch', kwargs={"branch_id": self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'


class GalleryBranches(models.Model):
    image = models.ImageField(upload_to='branches/', verbose_name='Фото/Лицензии/Схема проезда', blank=True)
    keyBranches = models.ForeignKey(Branches, on_delete=models.CASCADE, related_name='images')
    in_the_cont = models.BooleanField(default=False, verbose_name='В основной контент')
    location_map = models.BooleanField(default=False, verbose_name='Схема проезда')
    licenses = models.BooleanField(default=False, verbose_name='Лизензии')





