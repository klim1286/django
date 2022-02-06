from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractUser


class ShopUser(AbstractUser):
    age = models.PositiveIntegerField(verbose_name="Возраст")
    avatar = models.ImageField(verbose_name="Аватар", blank=True, upload_to="users")
    phone = models.CharField(verbose_name="телефон", blank=True, max_length=20)
    city = models.CharField(verbose_name="город", blank=True, max_length=20)
