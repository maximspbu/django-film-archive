# Generated by Django 5.0.6 on 2024-08-24 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("films", "0003_castcrew_alter_genre_options_alter_genre_name_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profession",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        choices=[
                            ("DIR", "Director"),
                            ("ACT", "Actor"),
                            ("PRD", "Producer"),
                            ("SND", "SoundTrack"),
                            ("EXC", "Executive"),
                            ("PD", "Production Designer"),
                            ("MDEP", "Music Department"),
                            ("WRT", "Writer"),
                        ],
                        max_length=30,
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
                "abstract": False,
            },
        ),
        migrations.RemoveField(
            model_name="film",
            name="cast_crew",
        ),
        migrations.AddField(
            model_name="film",
            name="actors",
            field=models.ManyToManyField(
                blank=True, related_name="actors_film", to="films.castcrew"
            ),
        ),
        migrations.AddField(
            model_name="film",
            name="directors",
            field=models.ManyToManyField(
                blank=True, related_name="directors_film", to="films.castcrew"
            ),
        ),
        migrations.RemoveField(
            model_name="castcrew",
            name="profession",
        ),
        migrations.AlterField(
            model_name="film",
            name="running_time",
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="castcrew",
            name="profession",
            field=models.ManyToManyField(to="films.profession"),
        ),
    ]
