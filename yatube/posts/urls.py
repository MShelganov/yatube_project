# posts/urls.py
from django.urls import path

from . import views

# Эта строчка обязательна.
# Без нее чуда не произойдет и namespace работать не будет
app_name = 'posts'

urlpatterns = [
    path('', views.index, name='main-view'),
    path('index/', views.index, name='main-view'),
    path('index.html', views.index, name='main-view'),
    path('group_list/', views.group_list),
    path('group_list.html', views.group_list, name='group_list'),
    path('group/<slug:slug>/', views.group_posts, name='group_posts'),
]
