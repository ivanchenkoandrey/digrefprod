# Generated by Django 3.2.12 on 2022-09-27 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0038_challenge_challengeparticipant_challengereport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(blank=True, default='', verbose_name='Текст'),
        ),
    ]
