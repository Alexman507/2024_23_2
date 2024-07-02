from django.core.cache import cache

from config.settings import CACHE_ENABLED
from main.models import Product, Category


def get_categories_from_cache():
    """
    Получение категорий из кэша. Если кэш пуст,то получение из БД.
    """
    if not CACHE_ENABLED:
        return Category.objects.all()
    else:
        key = 'categories_list'
        categories = cache.get(key)
        if categories is not None:
            return categories
        else:
            categories = Category.objects.all()
            cache.set(key, categories)
            return categories


def get_products_from_cache():
    """
    Получение продуктов из кэша. Если кэш пуст,то получение из БД.
    """
    if not CACHE_ENABLED:
        return Product.objects.all()
    else:
        key = 'products_list'
        products = cache.get(key)
        if products is not None:
            return products
        else:
            products = Product.objects.all()
            cache.set(key, products)
            return products
