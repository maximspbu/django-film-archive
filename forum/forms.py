from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import CustomUser


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


class LogInForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'email',
            'password',
        ]
