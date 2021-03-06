# Generated by Django 3.0.9 on 2020-09-21 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0004_auto_20200918_0712'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.TextField(verbose_name='Фамилия')),
                ('name', models.TextField(verbose_name='Имя')),
                ('patronymic', models.TextField(verbose_name='Отчество')),
                ('division', models.TextField(verbose_name='Подразделение (Наименование)')),
                ('job', models.TextField(verbose_name='Штатная должность (Наименование)')),
                ('vyz', models.TextField(verbose_name='ВУЗ')),
                ('date_vyz', models.TextField(verbose_name='Дата окончания')),
                ('profession', models.TextField(verbose_name='Специальность')),
                ('sertif', models.TextField(verbose_name='Сертификат')),
                ('date_sertif', models.TextField(verbose_name='Дата выдачи')),
                ('category', models.TextField(verbose_name='Категория')),
                ('degree', models.TextField(verbose_name='Степень')),
                ('keyBranches', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specialist', to='structure.Branches')),
            ],
            options={
                'verbose_name': 'Специалист',
                'verbose_name_plural': 'Специалисты',
            },
        ),
    ]
