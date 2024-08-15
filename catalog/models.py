from django.db import models

NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование категории")
    description = models.TextField(verbose_name="Описание категории", **NULLABLE)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ('name',)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование товара")
    description = models.TextField(verbose_name="Описание товара", **NULLABLE)
    photo = models.ImageField(
        upload_to="products/", verbose_name="Изображение (превью)", **NULLABLE
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        **NULLABLE,
        related_name="products",
    )
    price = models.IntegerField(verbose_name="Цена за покупку")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateField(
        auto_now=True, verbose_name="Дата последнего изменения", **NULLABLE
    )
    manufactured_at = models.DateField(verbose_name="Дата производства продукта", **NULLABLE)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = (
            "name",
            "updated_at",
        )

    def __str__(self):
        return f"{self.name} {self.category} {self.price}"
