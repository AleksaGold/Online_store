import json

from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    """Класс для кастомной команды, которая умеет заполнять данные в базу данных,
    при этом предварительно зачищать ее от старых данных"""

    @staticmethod
    def json_read_categories():
        """Загружает список категорий из файла формата json"""
        with open("category_data.json", "r") as file:
            return json.load(file)

    @staticmethod
    def json_read_products():
        """Загружает список продуктов из файла формата json"""
        with open("product_data.json", "r") as file:
            return json.load(file)

    def handle(self, *args, **options):
        """Команда для заполнения базы данных"""

        Category.objects.all().delete()
        Product.objects.all().delete()

        category_for_create = []
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(
                    pk=category["pk"],
                    name=category["fields"]["name"],
                    description=category["fields"]["description"],
                )
            )

        Category.objects.bulk_create(category_for_create)

        product_for_create = []
        for product in Command.json_read_products():
            product_for_create.append(
                Product(
                    pk=product["pk"],
                    name=product["fields"]["name"],
                    description=product["fields"]["description"],
                    photo=product["fields"]["photo"],
                    category=Category.objects.get(pk=product["fields"]["category"]),
                    price=product["fields"]["price"],
                    created_at=product["fields"]["created_at"],
                    updated_at=product["fields"]["updated_at"],
                )
            )

        Product.objects.bulk_create(product_for_create)
