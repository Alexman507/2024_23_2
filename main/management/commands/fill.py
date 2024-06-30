import json

from django.core.management import BaseCommand
from django.db import connection

from main.models import Category, Product, Contact, Order


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        categories = []
        # Здесь мы получаем данные из фикстур с категориями
        with open('data/main_data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

            for item in data:
                if item.get('model') == "main.category":
                    categories.append(item)
        return categories

    @staticmethod
    def json_read_products():
        products = []
        # Здесь мы получаем данные из фикстур с продуктами
        with open('data/main_data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

            for item in data:
                if item.get('model') == "main.product":
                    products.append(item)
        return products

    @staticmethod
    def json_read_contacts():
        contacts = []
        with open('data/main_data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

            for item in data:
                if item.get('model') == "main.contact":
                    contacts.append(item)
        return contacts

    @staticmethod
    def json_read_orders():
        orders = []
        with open('data/main_data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

            for item in data:
                if item.get('model') == "main.order":
                    orders.append(item)
        return orders

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            cursor.execute(f"TRUNCATE TABLE main_category RESTART IDENTITY CASCADE;")
            cursor.execute(f"TRUNCATE TABLE main_product RESTART IDENTITY CASCADE;")
            cursor.execute(f"TRUNCATE TABLE main_contact RESTART IDENTITY CASCADE;")
            cursor.execute(f"TRUNCATE TABLE main_order RESTART IDENTITY CASCADE;")
        # Удалите все продукты
        Product.objects.all().delete()

        # Удалите все категории
        Category.objects.all().delete()

        # Создайте списки для хранения объектов
        product_list = []
        category_list = []
        contact_list = []
        order_list = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_list.append(
                Category(
                    pk=category['pk'], name=category['fields']['name'],
                    description=category['fields']['description']
                )
            )

            # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_list)

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_list.append(
                Product(pk=product['pk'],
                        name=product['fields']['name'],
                        description=product['fields']['description'],
                        price=product['fields']['price'],
                        category=Category.objects.get(pk=product['fields']['category']),
                        preview=product['fields']['preview'],
                        created_at=product['fields']['created_at'],
                        updated_at=product['fields']['updated_at']))

            # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_list)

        for contact in Command.json_read_contacts():
            contact_list.append(
                Contact(pk=contact['pk'], name=contact['fields']['name'],
                        phone=contact['fields']['phone'],
                        inn=contact['fields']['inn'],
                        address=contact['fields']['address'],
                        ))

            # Создаем объекты в базе с помощью метода bulk_create()
        Contact.objects.bulk_create(contact_list)

        for order in Command.json_read_orders():
            order_list.append(
                Order(pk=order['pk'], name=order['fields']['name'],
                      phone=order['fields']['phone'],
                      message=order['fields']['message'],
                      created_at=order['fields']['created_at'],
                      ))

            # Создаем объекты в базе с помощью метода bulk_create()
        Order.objects.bulk_create(order_list)
