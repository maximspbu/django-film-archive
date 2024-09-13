from django.contrib import admin
from . import models


@admin.register(models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'first_name',
        'last_name',
        'registration_date',
        'is_active',
        'is_stuff',
        'is_superuser',
    )

@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'reply',
        'created_at',
    )

@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'film',
        'created_at',
    )

@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'created_at',
        'updated_at',
    )
