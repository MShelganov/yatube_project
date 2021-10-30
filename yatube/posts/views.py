# from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    """Main page"""
    return HttpResponse('Главная страница')


def group_posts(request: HttpRequest, slug: str) -> HttpResponse:
    """Load groups"""
    return HttpResponse(f'Главная страница {slug}')
