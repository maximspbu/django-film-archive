from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Film, CastCrew


class HomePage(ListView):
    model = Film
    template = 'films/film_list.html'
    context_object_name = 'film_list'
    paginate_by = 10

    def get_queryset(self) -> QuerySet[Any]:
        return self.model.objects.all()[:5]
    

class FilmDetail(DetailView):
    model = Film
    template = 'films/film_detail.html'


class CastCrewDetail(DetailView):
    model = CastCrew
    template = 'films/cast_crew_detail.html'
    context_object_name = 'castcrew'


class CastCrewList(ListView):
    model = CastCrew
    template = 'films/cast_crew_list.html'
    context_object_name = 'cast_crew_list'
