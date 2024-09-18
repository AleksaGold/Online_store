from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from catalog.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')

    avatar = models.ImageField(upload_to='user_avatar/', verbose_name="Аватар", **NULLABLE)
    phone_number = PhoneNumberField(verbose_name='Номер телефона', **NULLABLE)
    country = models.CharField(max_length=150, verbose_name='Страна', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
