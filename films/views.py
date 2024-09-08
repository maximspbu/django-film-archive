from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from .models import Film, CastCrew, FilmCastCrew
from .forms import SearchFilmForm


class HomePage(ListView):
    model = Film
    template = 'films/film_list.html'
    context_object_name = 'film_list'
    paginate_by = 20

    def get_queryset(self) -> QuerySet[Any]:
        queryset = Film.objects.all()
        form = SearchFilmForm(self.request.GET)
        if self.request.GET and form.is_valid():
            if form.cleaned_data.get('name'):
                if form.cleaned_data['name'].strip() == '':
                    return queryset
                queryset = queryset.filter(name__icontains=form.cleaned_data['name'])

        return queryset
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['form'] = SearchFilmForm(self.request.GET or None)
        return context
    

class FilmDetail(DetailView):
    model = Film
    template = 'films/film_detail.html'

    # def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
    #     return super().get_object(queryset)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cast_crew'] = FilmCastCrew.objects.filter(film=self.object)
        context['director'] = [i.cast_crew for i in context['cast_crew'] if i.profession.name=='Director'][0]
        context['actors'] = [i.cast_crew for i in context['cast_crew'] if i.profession.name=='Actor']
        return context


class CastCrewDetail(DetailView):
    model = CastCrew
    template = 'films/castcrew_detail.html'
    context_object_name = 'castcrew'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['films'] = [i.film for i in FilmCastCrew.objects.filter(cast_crew=self.object)]
        return context


class CastCrewList(ListView):
    model = CastCrew
    template = 'films/castcrew_list.html'
    context_object_name = 'castcrew_list'
    paginate_by = 20

    def get_queryset(self) -> QuerySet[Any]:
        return CastCrew.objects.all()
