from django.contrib import admin

from catalog.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Класс для настройки отображения модели "Категории" в административной панели"""

    list_display = (
        "pk",
        "name",
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Класс для настройки отображения модели "Продукты" в административной панели"""

    list_display = (
        "pk",
        "name",
        "price",
        "category",
    )
    list_filter = ("category",)
    search_fields = (
        "name",
        "description",
    )
