from django.core.management.base import BaseCommand

from mars_api.data_import.data_importer import import_data


class Command(BaseCommand):
    help = "Adds games and player scores to the database from the provided csv file"

    def add_arguments(self, parser):
        parser.add_argument(
            "csv_file_path",
            nargs="?",
            type=str,
            default="./mars_api/data_import/terra-mars-initial-data.csv",
        )

    def handle(self, *args, **options):
        import_data(options["csv_file_path"])
