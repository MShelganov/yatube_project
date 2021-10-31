# from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    """Main page. """
    temp = 'post/index.html'
    return render(request, temp)


def group_list(request: HttpRequest) -> HttpResponse:
    """List. """
    temp = 'post/group_list.html'
    return render(request, temp)


def group_posts(request: HttpRequest, slug: str) -> HttpResponse:
    """Load groups. """
    return HttpResponse(f'test group_posts {slug}')
