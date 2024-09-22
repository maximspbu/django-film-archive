from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import CustomUser, Topic


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'email',
            'first_name',
            'last_name',
            'bio',
            'avatar',

        ]

class TopicCreateForm(ModelForm):
    class Meta:
        model = Topic
        fields = [
            'title',
            #'author',
            'text',
        ]
