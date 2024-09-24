from django.db import models
from django.urls import reverse

GENRES = {
    "ACT": "Action",
    "ADV": "Adventure",
    "ANM": "Animated",
    "BIO": "Biography",
    "COM": "Comedy",
    "CRM": "Crime",
    "DET": "Detective",
    "DOC": "Documentary",
    "DRM": "Drama",
    "EPC": "Epic",
    "FAM": "Family",
    "FAN": "Fantasy",
    "FN": "Film-Hoir",
    "HIS": "History",
    "HOR": "Horror",
    "MUS": "Musical",
    "MYS": "Mystery",
    "ROM": "Romance",
    "SF": "Sci-Fi",
    "SPT": "Sport",
    "TLR": "Thriller",
    "WAR": "War",
    "WST": "Western",
}

PROFESSIONS = {
    "DIR": "Director",
    "ACT": "Actor",
    "PRD": "Producer",
    "SND": "SoundTrack",
    "EXC": "Executive",
    "PD": "Production Designer",
    "MDEP": "Music Department",
    "WRT": "Writer",
}


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ["name"]


class Profession(Category):
    name = models.CharField(max_length=30, choices=PROFESSIONS.items())


class Genre(Category):
    name = models.CharField(max_length=30, choices=GENRES.items())


class CastCrew(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField(blank=True, null=True)
    professions = models.ManyToManyField("Profession")  # type: Profession

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse(
            "cast_crew_detail", args=[str(self.id)]
        )  # /myapplication/mymodelname/2

    def display_admin_profession(self):
        """returns string that display profession for admin panel"""
        return ", ".join(prof.name for prof in self.professions.all()[:3])

    display_admin_profession.short_description = "Profession"

    class Meta:
        ordering = ["last_name", "first_name"]


class Film(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=100, unique=True)
    storyline = models.TextField(max_length=1000, blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    running_time = models.DurationField(blank=True, null=True)
    budget = models.BigIntegerField(blank=True, null=True)
    box_office = models.BigIntegerField(blank=True, null=True)
    cover = models.ImageField(blank=True, null=True)
    genres = models.ManyToManyField("Genre", blank=True)  # type: Genre

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            "film_detail", args=[str(self.id)]
        )  # /myapplication/mymodelname/2

    def display_admin_genre(self):
        """returns string that display genre for admin panel"""
        return ", ".join(genre.name for genre in self.genres.all()[:3])

    display_admin_genre.short_description = "Genre"

    class Meta:
        ordering = ["-release_date"]


class FilmCastCrew(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    cast_crew = models.ForeignKey(CastCrew, on_delete=models.CASCADE)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cast_crew} in {self.film} as {self.profession}"
