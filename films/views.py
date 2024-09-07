from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from .models import Film, CastCrew, FilmCastCrew


class HomePage(ListView):
    model = Film
    template = 'films/film_list.html'
    context_object_name = 'film_list'
    paginate_by = 20

    def get_queryset(self) -> QuerySet[Any]:
        #film_ids = self.model.objects.values_list('film', flat=True).distinct()
        #print([i for i in film_ids])
        #print(set([getattr(i, 'film') for i in FilmCastCrew.objects.filter(film__id__in=film_ids)]))
        return Film.objects.all()
        #return self.model.objects.filter(film__in=self.model.objects.select_related('film').values('name')).distinct()
    

class FilmDetail(DetailView):
    model = Film
    template = 'films/film_detail.html'

    # def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
    #     return super().get_object(queryset)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Получаем список участников через FilmCastCrew, фильтруя по текущему фильму
        context['cast_crew'] = FilmCastCrew.objects.filter(film=self.object)
        #print([i.profession for i in context['cast_crew']])
        context['director'] = [i.cast_crew for i in context['cast_crew'] if i.profession.name=='Director'][0]
        context['actors'] = [i.cast_crew for i in context['cast_crew'] if i.profession.name=='Actor']
        return context


class CastCrewDetail(DetailView):
    model = CastCrew
    template = 'films/castcrew_detail.html'
    context_object_name = 'castcrew'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Получаем список участников через FilmCastCrew, фильтруя по текущему фильму
        context['films'] = [i.film for i in FilmCastCrew.objects.filter(cast_crew=self.object)]
        return context


class CastCrewList(ListView):
    model = CastCrew
    template = 'films/castcrew_list.html'
    context_object_name = 'cast_crew_list'
    paginate_by = 20

    def get_queryset(self) -> QuerySet[Any]:
        return CastCrew.objects.all()
