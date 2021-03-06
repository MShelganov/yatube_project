# Generated by Django 2.2.9 on 2021-11-05 01:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20211104_0012'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-pub_date', 'author']},
        ),
        migrations.AlterField(
            model_name='group',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.SlugField(max_length=200, unique=True, verbose_name='Подзаголовок'),
        ),
        migrations.AlterField(
            model_name='group',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='post',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='groups', to='posts.Group', verbose_name='Группа'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(verbose_name='Текст'),
        ),
        migrations.AddIndex(
            model_name='group',
            index=models.Index(fields=['title'], name='title_idx'),
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['author'], name='author_idx'),
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['text'], name='search_text_idx'),
        ),
        migrations.AlterModelTable(
            name='group',
            table='groups',
        ),
        migrations.AlterModelTable(
            name='post',
            table='posts',
        ),
    ]
