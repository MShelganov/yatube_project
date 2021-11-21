from django.conf import settings
from django.contrib import admin

from .models import Group, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group',
    )
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = settings.EMPTY_STR


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    view_on_site = True
    list_display = (
        'pk',
        'title',
        'slug',
        'description',
    )
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    empty_value_display = settings.EMPTY_STR
