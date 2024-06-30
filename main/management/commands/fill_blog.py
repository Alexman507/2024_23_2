import json

from django.core.management import BaseCommand
from django.db import connection

from blog.models import Blog


class Command(BaseCommand):

    @staticmethod
    def json_read_blogs():
        items = []
        # Здесь мы получаем данные из фикстур с продуктами
        with open('data/blog_data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

            for item in data:
                if "blog.blog" in item.get('model'):
                    if item.get('model') == "blog.blog":
                        items.append(item)
        return items

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            cursor.execute(f"TRUNCATE TABLE main_category RESTART IDENTITY CASCADE;")
            cursor.execute(f"TRUNCATE TABLE main_product RESTART IDENTITY CASCADE;")
            cursor.execute(f"TRUNCATE TABLE main_contact RESTART IDENTITY CASCADE;")
            cursor.execute(f"TRUNCATE TABLE main_order RESTART IDENTITY CASCADE;")

        Blog.objects.all().delete()

        # Создайте списки для хранения объектов
        blog_list = []

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for blog in Command.json_read_blogs():
            blog_list.append(
                Blog(pk=blog['pk'],
                     title=blog['fields']['title'],
                     slug=blog['fields']['slug'],
                     content=blog['fields']['content'],
                     preview=blog['fields']['preview'],
                     created_at=blog['fields']['created_at'],
                     published=blog['fields']['published'],
                     views=blog['fields']['views']
                     ))

            # Создаем объекты в базе с помощью метода bulk_create()
        Blog.objects.bulk_create(blog_list)
