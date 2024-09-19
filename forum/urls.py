from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='forum_home'),
    path('users/<pk>/', views.UserDetailView.as_view(), name='user_detail'),
    #path('users/<pk:int>/chat/', views.ChatDetailView.as_view(), name='user_detail'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.LogInView.as_view(), name='login'),
    path('users/', views.UserListView.as_view(), name='user_list'),
    path('topics/<pk>/', views.TopicDetailView.as_view(), name='topic_detail'),
    path('topics/', views.TopicListView.as_view(), name='topic_list'),
    path('reviews/<pk>/', views.ReviewDetailView.as_view(), name='review_detail'),
    path('reviews/', views.ReviewListView.as_view(), name='review_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
