# Generated by Django 3.2.12 on 2022-09-10 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0029_alter_likestatistics_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='first_comment',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='is_commentable',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='last_comment',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='last_dislike_change_at',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='last_event_comment',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='last_like_change_at',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='last_like_or_comment_change_at',
        ),
        migrations.CreateModel(
            name='LikeCommentStatistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_like_or_comment_change_at', models.DateTimeField(blank=True, null=True, verbose_name='Время последнего изменения количества лайков или последнего добавления/изменения комментария')),
                ('comment_counter', models.IntegerField(verbose_name='Количество комментариев')),
                ('first_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='first_comment_statistics', to='auth_app.comment', verbose_name='Первый комментарий')),
                ('last_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_comment_statistics', to='auth_app.comment', verbose_name='Последний комментарий')),
                ('last_event_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_event_comment_statistics', to='auth_app.comment', verbose_name='Последний добавленный или измененный комментарий')),
                ('transaction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='like_comment_statistics', to='auth_app.transaction', verbose_name='Транзакция')),
            ],
            options={
                'db_table': 'like_comment_statistics',
            },
        ),
    ]