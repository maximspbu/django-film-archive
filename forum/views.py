from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, FormView

from .forms import SignUpForm, TopicCreateForm
from .models import CustomUser, Review, Topic


class Home(TemplateView):
    template_name = "forum/index.html"

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        form = SignUpForm(request.GET or None)
        if request.GET and form.is_valid():
            return super().get(request, *args, **kwargs)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["form"] = SignUpForm(self.request.GET or None)
        return context


class SignUpView(SuccessMessageMixin, CreateView):
    template_name = "forum/signup.html"
    form_class = SignUpForm
    success_url = "/success/"
    success_message = "Your profile was created successfully"

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        return super().get(request, *args, **kwargs)


class LogInView(TemplateView):
    template_name = "forum/login.html"


class UserDetailView(DetailView):
    model = CustomUser
    template = "forum/customuser_detail.html"
    context_object_name = "customuser"


class UserListView(ListView):
    model = CustomUser
    template = "forum/customuser_list.html"
    context_object_name = "customuser_list"
    paginate_by = 20


class TopicDetailView(DetailView):
    model = Topic
    template = "forum/topic_detail.html"
    context_object_name = "topic"


class TopicListView(ListView):
    model = Topic
    template = "forum/topic_list.html"
    context_object_name = "topic_list"
    paginate_by = 20


class ReviewDetailView(DetailView):
    model = Review
    template = "forum/review_detail.html"
    context_object_name = "review"


class ReviewListView(ListView):
    model = Review
    template = "forum/review_list.html"
    context_object_name = "review_list"
    paginate_by = 20


class TopicCreateView(LoginRequiredMixin, FormView):
    form_class = TopicCreateForm
    template_name = "forum/topic_create.html"
    success_url = reverse_lazy("topic_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)
        # return super(TopicCreateView, self).form_valid(form)
