# Generated by Django 3.2.12 on 2022-10-10 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0044_alter_transactionstate_controller'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='object_selector',
            field=models.CharField(blank=True, choices=[('T', 'Транзакция'), ('Q', 'Quest'), ('R', 'Report'), ('N', 'News'), ('A', 'Объявление')], max_length=1, null=True, verbose_name='Селектор объекта'),
        ),
    ]
