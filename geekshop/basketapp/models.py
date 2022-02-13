from django.db import models
from django.conf import settings
from mainapp.models import Product


class BasketManadger(models.Manager):
    def total_quantity(self):
        basket_items = self.all()
        return sum(item.quantity for item in basket_items)

    def total_cost(self):
        basket_items = self.all()
        return sum(item.cost for item in basket_items)


class Basket(models.Model):
    class Meta:
        unique_together = ["user", "product"]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="basket"
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name="количество", default=0)
    add_datetime = models.DateTimeField(verbose_name="время", auto_now_add=True)

    objects = BasketManadger()

    @property
    def cost(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product.name} - {self.quantity} шт."
