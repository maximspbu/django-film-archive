from django.urls import include, path
from .views import HomePage, FilmDetail


urlpatterns = [
    path('', HomePage.as_view(), name='films_home'),
    path('<int:pk>/', FilmDetail.as_view(), name='film_detail'),
]
