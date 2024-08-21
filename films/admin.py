from django.contrib import admin
from .models import Genre, Film, CastCrew


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'release_date', 'display_admin_genre', 'budget', 'box_office')

@admin.register(CastCrew)
class CastCrewAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'birth_date', 'profession')
