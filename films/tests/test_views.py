import os
from django import setup

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "film_archive.settings")
setup()

from django.test import TestCase
from ..models import Film
from datetime import datetime, timedelta



class FilmListViewTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        number_of_films = 100
        for film_num in range(number_of_films):
            Film.objects.create(
                name=f'Film#{film_num}',
                storyline='Some text.',
                release_date=datetime.today().strftime('%Y-%m-%d'),
                running_time=timedelta(hours=2, minutes=30),
                budget=100000000,
                box_office=523221337,
            )
    
    def test_view_exists(self):
        response = self.client.get('/films/home/')
        self.assertEqual(response.status_code, 200)
