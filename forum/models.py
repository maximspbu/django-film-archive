from datetime import date, datetime

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Invalid email!")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=320, unique=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    bio = models.TextField(max_length=600, blank=True, null=True)
    registration_date = models.DateField(default=date.today)
    avatar = models.ImageField(upload_to="images/avatars", blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("user_detail", args=[str(self.id)])

    class Meta:
        ordering = ["id"]


class BaseContent(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse(f"{self._meta.model_name.lower()}_detail", args=[str(self.id)])

    class Meta:
        ordering = ["id"]  # '-created_at'
        abstract = True


# class FileContent(models.Model):
#     content = models.ForeignKey(BaseContent, on_delete=models.CASCADE)
#     file = models.FileField(upload_to='media')


class Message(BaseContent):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    related_object = GenericForeignKey("content_type", "object_id")
    reply = models.ForeignKey(
        "Message", blank=True, null=True, on_delete=models.CASCADE
    )


class Review(BaseContent):
    film = models.ForeignKey("films.Film", on_delete=models.CASCADE)


class Topic(BaseContent):
    updated_at = models.DateTimeField(default=datetime.now)
