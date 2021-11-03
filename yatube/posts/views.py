# from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request: HttpRequest) -> HttpResponse:
    """Main page. """
    temp = 'post/index.html'
    title = 'Последние обновления на сайте'
    posts = Post.objects.order_by('-pub_date')[:10]
    # Словарь с данными принято называть context
    context = {
        'title': title,
        'posts': posts,
    }
    # Третьим параметром передаём словарь context
    return render(request, temp, context)


def group_posts(request: HttpRequest, slug: str) -> HttpResponse:
    """View-функция для страницы сообщества. """
    # Функция get_object_or_404 получает по заданным критериям объект
    # из базы данных или возвращает сообщение об ошибке, если объект не найден.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе
    group = get_object_or_404(Group, slug=slug)
    temp = 'post/group_list.html'
    title = f'Записи сообщества {group.title}'
    # Метод .filter позволяет ограничить поиск по критериям.
    # Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'title': title,
        'group': group,
        'posts': posts,
    }
    return render(request, temp, context)
