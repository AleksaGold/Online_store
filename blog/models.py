from django.db import models

from catalog.models import NULLABLE


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    slug = models.CharField(max_length=150, verbose_name="Slug", **NULLABLE)
    content = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(
        upload_to="blog/", verbose_name="Превью (изображение)", **NULLABLE
    )
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")
    views_count = models.PositiveIntegerField(
        default=0, verbose_name="Количество просмотров"
    )

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = (
            "created_at",
            "views_count",
        )

    def __str__(self):
        return f'{self.title}'
