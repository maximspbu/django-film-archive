from django.urls import include, path
from .views import HomePage, FilmDetail, CastCrewDetail, CastCrewList


urlpatterns = [
    path('home/', HomePage.as_view(), name='films_home'),
    path('film/<int:pk>/', FilmDetail.as_view(), name='film_detail'),
    path('cast_crew/', CastCrewList.as_view(), name='cast_crew_list'),
    path('cast_crew/<int:pk>', CastCrewDetail.as_view(), name='cast_crew_detail'),
]
