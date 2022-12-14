# Generated by Django 3.2.12 on 2022-09-30 11:16

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0040_auto_20220929_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='participants_count',
            field=models.PositiveIntegerField(default=0, verbose_name='Текущее количество участников'),
        ),
        migrations.AddField(
            model_name='challenge',
            name='winners_count',
            field=models.PositiveIntegerField(default=0, verbose_name='Текущее количество победителей'),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='challenge_mode',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('O', 'От имени организации'), ('U', 'От имени пользователя'), ('P', 'Является публичным'), ('C', 'Является командным'), ('R', 'Нужна регистрация'), ('G', 'Нужна картинка'), ('M', 'Запрет комментариев'), ('E', 'Разрешить комментарии только для участников'), ('L', 'Лайки запрещены'), ('T', 'Разрешить лайки только для участников'), ('X', 'Комментарии отчетов разрешены только автору отчета, организатору и судьям'), ('W', 'Комментарии отчетов разрешены только участникам'), ('I', 'Лайки отчетов разрешены только участникам'), ('N', 'Участник может использовать никнейм'), ('H', 'Участник может сделать отчёт приватным'), ('A', 'Отчеты анонимизированы до подведения итогов, не видны ни имена пользователей, ни псевдонимы'), ('Q', 'Участник может рассылать приглашения'), ('Y', 'Подтверждение будет выполняться судейской коллегией (через выдачу ими баллов)'), ('K', 'Максимум 1 отчет для отправки для каждого участника')], max_length=1), blank=True, null=True, size=20),
        ),
    ]
