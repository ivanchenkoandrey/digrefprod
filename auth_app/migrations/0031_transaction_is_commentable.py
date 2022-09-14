# Generated by Django 3.2.12 on 2022-09-10 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0030_auto_20220910_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='is_commentable',
            field=models.BooleanField(default=True, verbose_name='Разрешение на добавление/изменение/удаления комментариев'),
        ),
    ]