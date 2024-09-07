from django.test import TestCase
from films.models import Film
from datetime import datetime, timedelta

class FilmModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls) -> None:
        Film.objects.create(
            name='FilmModelTest',
            storyline='Some text.',
            release_date=datetime.today().strftime('%Y-%m-%d'),
            running_time=timedelta(hours=2, minutes=30),
            budget=100000000,
            box_office=523221337,
        )

    def test_check_release_date(self):
        film = Film.objects.get(pk=1)
        self.assertLessEqual(film.release_date.strftime('%Y-%m-%d'), datetime.today().strftime('%Y-%m-%d'))
