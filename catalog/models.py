from django.db import models

NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    """Класс для описания модели "Категории" """

    name = models.CharField(max_length=150, verbose_name="Наименование категории")
    description = models.TextField(verbose_name="Описание категории", **NULLABLE)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ("name",)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    """Класс для описания модели "Продукты" """

    name = models.CharField(max_length=150, verbose_name="Наименование товара")
    description = models.TextField(verbose_name="Описание товара", **NULLABLE)
    photo = models.ImageField(
        upload_to="catalog/", verbose_name="Изображение (превью)", **NULLABLE
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        **NULLABLE,
        related_name="catalog",
    )
    price = models.IntegerField(verbose_name="Цена за покупку")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateField(
        auto_now=True, verbose_name="Дата последнего изменения", **NULLABLE
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = (
            "name",
            "updated_at",
        )

    def __str__(self):
        return f"{self.name} {self.category} {self.price}"


class Version(models.Model):
    """Класс для описания модели "Версии продукта" """

    version_number = models.PositiveIntegerField(default=1, verbose_name="Номер версии")
    name = models.CharField(max_length=150, verbose_name="Название версии")
    is_current_version = models.BooleanField(
        default=False, verbose_name="Текущая версия"
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Продукт",
        related_name="product",
        **NULLABLE,
    )

    class Meta:
        verbose_name = "Версия продукта"
        verbose_name_plural = "Версии продуктов"
        ordering = ("version_number",)

    def __str__(self):
        return f"{self.name} {self.is_current_version} {self.product}"
