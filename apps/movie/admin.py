from django.contrib import admin
from .models import *


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'active']


@admin.register(TagModel)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'url']


@admin.register(ActorModel)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['name', 'url']


@admin.register(MovieModel)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'age', 'grade']


@admin.register(MoviePartModel)
class MoviePartAdmin(admin.ModelAdmin):
    list_display = ['base', 'title', 'time', 'like']


@admin.register(SeriesModel)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'grade']


@admin.register(SeriesSeasonModel)
class SerialSeasonAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(SeriesPartModel)
class SeriesParAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']
