# Generated by Django 3.0.9 on 2020-09-04 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Наименование')),
                ('address', models.TextField(blank=True, verbose_name='Адрес')),
                ('phones', models.IntegerField(verbose_name='Телефоны')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('content', models.TextField(blank=True, verbose_name='Контент')),
            ],
            options={
                'verbose_name': 'Филиал',
                'verbose_name_plural': 'Филиалы',
            },
        ),
        migrations.CreateModel(
            name='GalleryBranches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='branches/', verbose_name='Фото/Лицензии/Схема проезда')),
                ('in_the_cont', models.BooleanField(default=False, verbose_name='В основной контент')),
                ('location_map', models.BooleanField(default=False, verbose_name='Схема проезда')),
                ('licenses', models.BooleanField(default=False, verbose_name='Лизензии')),
                ('keyBranches', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='structure.Branches')),
            ],
        ),
    ]
