# from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    """Main page. """
    temp = 'post/index.html'
    title = 'Это главная страница проекта Yatube'
    # Словарь с данными принято называть context
    context = {
        'title': title,
    }
    # Третьим параметром передаём словарь context
    return render(request, temp, context)


def group_list(request: HttpRequest) -> HttpResponse:
    """List. """
    temp = 'post/group_list.html'
    title = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'title': title,
    }
    return render(request, temp, context)


def group_posts(request: HttpRequest, slug: str) -> HttpResponse:
    """Load groups. """
    return HttpResponse(f'test group_posts {slug}')
