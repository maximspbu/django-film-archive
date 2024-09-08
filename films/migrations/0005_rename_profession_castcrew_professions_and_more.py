# Generated by Django 5.0.6 on 2024-08-26 06:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0004_profession_remove_film_cast_crew_film_actors_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='castcrew',
            old_name='profession',
            new_name='professions',
        ),
        migrations.RemoveField(
            model_name='film',
            name='actors',
        ),
        migrations.RemoveField(
            model_name='film',
            name='directors',
        ),
        migrations.CreateModel(
            name='FilmCastCrew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cast_crew', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.castcrew')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.film')),
                ('profession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.profession')),
            ],
        ),
    ]
