from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Group, Post


def index(request: HttpRequest) -> HttpResponse:
    """Main page. """
    temp = 'posts/index.html'
    title = 'Последние обновления на сайте'
    posts = Post.objects.all()[:10]
    context = {
        'title': title,
        'posts': posts,
    }
    return render(request, temp, context)


def group_posts(request: HttpRequest, slug: str) -> HttpResponse:
    """View-функция для страницы сообщества. """
    group = get_object_or_404(Group, slug=slug)
    temp = 'posts/group_list.html'
    title = f'Записи сообщества {group.title}'
    posts = group.groups.all()[:10]
    context = {
        'title': title,
        'group': group,
        'posts': posts,
    }
    return render(request, temp, context)
