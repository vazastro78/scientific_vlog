from django.core.management import BaseCommand

from config import settings
from newsblog.models import Article

import json
import codecs
import os

def get_field_list(filename='dump.json'):
    field_list = []
    with codecs.open(filename, encoding="utf8") as f:
        data = json.load(f)
        for item in data:
            field_list.append(item["fields"])
    return field_list


class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        запуск отдельной функции
        """
        self.clear_databases()
        self.handle_bulk_create(*args, **options)

    def clear_databases(self):
        Article.objects.all().delete()

    def handle_bulk_create(self, *args, **options):
        """
        заполнение с одним обращением в базу данных с
        записью множества строк одновременно
        """
        filename = os.path.join(settings.BASE_DIR, "newsblog", "management", "commands", "dump.json")
        field_list = get_field_list(filename)

        field_for_create = []
        for field_item in field_list:
            field_for_create.append(Article(**field_item))
        Article.objects.bulk_create(field_for_create)


