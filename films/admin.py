from django.contrib import admin
from .models import Genre, Film


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'release_date', 'display_admin_genre', 'budget', 'box_office')
