from django.db import models
from django.conf import settings
from mainapp.models import Product

class BasketQuerySet(models.query.QuerySet):
    def delete(self, *args, **kwargs):
        for item in self:
            item.product.quantity += item.quantity
            item.product.save()
        super().save(*args, **kwargs)


class BasketManadger(models.Manager):
    def total_quantity(self):
        basket_items = self.all()
        return sum(item.quantity for item in basket_items)

    def total_cost(self):
        basket_items = self.all()
        return sum(item.cost for item in basket_items)

    def get_queryset(self):
        return BasketQuerySet(self.model, using=self._db)


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

    def delete(self, *args, **kwargs):
        self.product.quantity += self.quantity
        self.product.save()
        super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.pk:
            old_basket = Basket.objects.get(pk=self.product.pk)
            self.product.quantity -= self.quantity - old_basket.quantity
        else:
            self.product.quantity -= self.quantity
        self.product.save()
        super().save(*args, **kwargs)


    @property
    def cost(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product.name} - {self.quantity} шт."
