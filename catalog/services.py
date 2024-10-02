from django.core.cache import cache

from catalog.models import Category, Product
from config.settings import CACHE_ENABLED


def get_categories_from_cache():
    """Получает данные по категориям из кэша, если кэш пустой, получает данные из БД"""
    if not CACHE_ENABLED:
        return Category.objects.all()
    categories_from_cache = "categories_list"
    categories = cache.get(categories_from_cache)
    if categories is not None:
        return categories
    categories = Category.objects.all()
    cache.set(categories_from_cache, categories)
    return categories


def get_products_from_cache():
    """Получает данные по продуктам из кэша, если кэш пустой, получает данные из БД"""
    if not CACHE_ENABLED:
        return Product.objects.all()
    products_from_cache = "products_list"
    products = cache.get(products_from_cache)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(products_from_cache, products)
    return products
