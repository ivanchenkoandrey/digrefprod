# Generated by Django 3.2.12 on 2022-11-09 14:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth_app', '0056_fcmtoken'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_user', models.PositiveIntegerField(blank=True, null=True, verbose_name='Инициировавший событие пользователь')),
                ('type', models.CharField(choices=[('L', 'Лайк'), ('C', 'Комментарий'), ('H', 'Челлендж'), ('T', 'Перевод'), ('W', 'Победа в челлендже'), ('R', 'Отправлен отчёт')], max_length=1, verbose_name='Тип уведомления')),
                ('object_id', models.PositiveIntegerField(blank=True, null=True, verbose_name='Идентификатор связанного объекта')),
                ('data', models.JSONField(blank=True, null=True, verbose_name='Данные, переданные с уведомлением')),
                ('theme', models.CharField(max_length=255, verbose_name='Тема')),
                ('text', models.TextField(verbose_name='Текст')),
                ('read', models.BooleanField(default=False, verbose_name='Прочитано')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Изменено')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'db_table': 'notifications',
            },
        ),
    ]