from django.db import models
from django.urls import reverse


GENRES = [
    ('ACT', 'Action'),
    ('ADV', 'Adventure'),
    ('ANM', 'Animated'),
    ('BIO', 'Biography'),
    ('COM', 'Comedy'),
    ('CRM', 'Crime'),
    ('DET', 'Detective'),
    ('DOC', 'Documentary'),
    ('DRM', 'Drama'),
    ('EPC', 'Epic'),
    ('FAM', 'Family'),
    ('FAN', 'Fantasy'),
    ('FN', 'Film-Hoir'),
    ('HIS', 'History'),
    ('HOR', 'Horror'),
    ('MUS', 'Musical'),
    ('MYS', 'Mystery'),
    ('ROM', 'Romance'),
    ('SF', 'Sci-Fi'),
    ('SPT', 'Sport'),
    ('TLR', 'Thriller'),
    ('WAR', 'War'),
    ('WST', 'Western'),
]


class Genre(models.Model):
    genre = models.CharField(max_length=30)


    def __str__(self):
        return self.genre


    class Meta:
        ordering = ["genre"]


class Film(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=100, unique=True)
    storyline = models.TextField(max_length=1000, blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    running_time = models.DateTimeField(blank=True, null=True)
    budget = models.BigIntegerField(blank=True, null=True)
    box_office = models.BigIntegerField(blank=True, null=True)
    cover = models.ImageField(blank=True, null=True)
    genres = models.ManyToManyField('Genre', blank=True) # models.CharField(max_length=30, choices=GENRES)
    # director = models.ForeignKey('CastCrew', on_delete=models.SET_NULL, blank=True, null=True)
    # actors = models.ManyToManyField('CastCrew', blank=True, null=True)


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('film_detail', args=[str(self.id)]) # /myapplication/mymodelname/2


    class Meta:
        ordering = ["-release_date"]
        