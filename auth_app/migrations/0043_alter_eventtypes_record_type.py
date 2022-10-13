# Generated by Django 3.2.12 on 2022-10-10 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0042_auto_20221007_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventtypes',
            name='record_type',
            field=models.CharField(blank=True, choices=[('S', 'Статус транзакции'), ('L', 'Лайк'), ('C', 'Комментарий'), ('R', 'Отчёт челленджа')], max_length=1, null=True, verbose_name='Тип записи о событии'),
        ),
    ]
