# Generated by Django 3.2.12 on 2022-10-07 14:53

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0041_auto_20220930_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstat',
            name='sent_to_challenges_from_income',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10, verbose_name='Пользователь отправил в фонды челленджей со счёта получения'),
        ),
        migrations.AlterField(
            model_name='challengeparticipant',
            name='mode',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('A', 'Запись актуальна'), ('Q', 'Приглашение'), ('P', 'Пользователь подтвердил участие'), ('H', 'Скрыть связь с пользователем'), ('R', 'Судья'), ('O', 'Организатор'), ('W', 'Победитель')], max_length=1), size=6),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_class',
            field=models.CharField(choices=[('T', 'Благодарность'), ('X', 'За стаж работы'), ('D', 'Для распределения'), ('R', 'Для перераспределения'), ('B', 'Сгорание'), ('O', 'Для расчета премии'), ('P', 'Покупка'), ('E', 'Эмитирование'), ('С', 'Погашение'), ('H', 'Для взноса в челлендж'), ('W', 'Награда из челленджа'), ('F', 'Возврат из челленджа')], max_length=1, verbose_name='Вид транзакции'),
        ),
        migrations.AlterField(
            model_name='userstat',
            name='sent_to_challenges',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10, verbose_name='Пользователь отправил в фонды челленджей со счёта раздачи'),
        ),
    ]
