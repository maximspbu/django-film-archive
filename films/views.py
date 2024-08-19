from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Film


class HomePage(ListView):
    model = Film
    template = 'films/film_list.html'
    context_object_name = 'film_list'

    def get_queryset(self) -> QuerySet[Any]:
        return self.model.objects.all()[:5]
    
    # def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    #     return super().get_context_data(**kwargs)  # 1) get context from super class 2) update context 3) return updated context

class FilmDetail(DetailView):
    model = Film
    template = 'films/film_detail.html'


