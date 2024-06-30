from django.contrib import admin

from django.contrib import admin
from main.models import Category, Product, Contact, Order

"""
Для категорий выводит **id** и **наименование** в список отображения, 
а для продуктов выводит в список **id**, **название**, **цену** и **категорию**.

Интерфейс вывода продуктов:
- результат отображения фильтровать по категории, 
- поиск по названию и полю описания.
"""


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category")
    list_filter = ("category",)
    search_fields = ("name", "description")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Contact)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "phone", "inn", "address",)
    search_fields = ("id", "name", "phone", "inn", "address",)


@admin.register(Order)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "phone", "message", "created_at",)
    search_fields = ("id", "name", "phone",)
