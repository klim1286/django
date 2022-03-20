from distutils.command.upload import upload
from email.mime import image
from turtle import color
from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=100)
    description = models.TextField(verbose_name="Описание", blank=True)

    def __str__(self):
        return self.name


class ProductManager(models.Manager):

    def active_items(self):
        return Product.objects.filter(is_active=True)


class Product(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=100)
    price = models.DecimalField(
        verbose_name="Цена", max_digits=7, decimal_places=2, default=0
    )
    color = models.CharField(verbose_name="Цвет", max_length=8, default="0x000000")
    description = models.TextField(verbose_name="Описание", blank=True)
    image = models.ImageField(verbose_name="Картинка", blank=True, upload_to="products")
    quantity = models.PositiveIntegerField(verbose_name="Количество", default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    is_active = models.BooleanField(verbose_name="Активный", default=True)

    objects = ProductManager()

    def __str__(self):
        return self.name
