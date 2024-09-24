from django.contrib import admin

from .models import CastCrew, Film, FilmCastCrew, Genre, Profession


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "release_date",
        "running_time",
        "display_admin_genre",
        "budget",
        "box_office",
    )


@admin.register(CastCrew)
class CastCrewAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "birth_date",
        "display_admin_profession",
    )


@admin.register(FilmCastCrew)
class FilmCastCrewAdmin(admin.ModelAdmin):
    list_display = (
        "film",
        "cast_crew",
        "profession",
    )
