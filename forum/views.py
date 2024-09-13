from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView
from .models import CustomUser, Topic, Review


class Home(TemplateView):
    template_name = 'forum/index.html'


class UserDetailView(DetailView):
    model = CustomUser
    template = 'forum/user_detail.html'


class UserListView(ListView):
    model = CustomUser
    template = 'forum/user_list.html'


class TopicDetailView(DetailView):
    model = Topic
    template = 'forum/topic_detail.html'


class TopicListView(ListView):
    model = Topic
    template = 'forum/topic_list.html'


class ReviewDetailView(DetailView):
    model = Review
    template = 'forum/review_detail.html'


class ReviewListView(ListView):
    model = Review
    template = 'forum/review_list.html'
