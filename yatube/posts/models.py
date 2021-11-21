import textwrap as tw

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


User = get_user_model()


class Post(models.Model):
    text = models.TextField('Текст')
    pub_date = models.DateTimeField('Дата', auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор'
    )
    group = models.ForeignKey(
        'Group',
        related_name='groups',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Группа'
    )

    class Meta:
        db_table = 'posts'
        ordering = ('-pub_date', 'author',)
        indexes = (
            models.Index(fields=['author'], name='author_idx'),
            models.Index(fields=['text'], name='search_text_idx'),
        )

    def __str__(self):
        # Обрезает тест до длины, меньшей или равной 40-и,
        # между границами слов, чтобы не было частичных слов.
        return tw.shorten(self.text, 40, placeholder='...')


class Group(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    slug = models.SlugField('Подзаголовок', max_length=200, unique=True)
    description = models.TextField('Описание', default='', blank=True)

    class Meta:
        db_table = 'groups'
        ordering = ('title',)
        indexes = (models.Index(fields=['title'], name='title_idx'),)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Получаю url из posts/urls.py по имени.
        return reverse('posts:group_list', kwargs={'slug': self.slug})
