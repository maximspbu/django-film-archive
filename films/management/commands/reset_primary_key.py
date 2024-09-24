from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    help = "Resets primary key sequence for a given model"

    def add_arguments(self, parser):
        parser.add_argument("model_name", type=str)

    def handle(self, *args, **options):
        model_name = options["model_name"]
        cursor = connection.cursor()
        cursor.execute(
            f"SELECT setval(pg_get_serial_sequence('{model_name}', 'id'), coalesce(max(id), 1), max(id) IS NOT null) FROM {model_name};"
        )
        self.stdout.write(
            self.style.SUCCESS(f"Successfully reset primary key for {model_name}")
        )
