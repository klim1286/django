from itertools import product
from django.conf import settings
from django.db import models
from mainapp.models import Product
from basketapp.models import Basket


class Order(models.Model):
    class Meta:
        verbose_name = "заказ"
        verbose_name_plural = "заказы"
        ordering = ("-created",)

    CREATED = "CREATED"
    IN_PROCESSING = "IN_PROCESSING"
    AWAITING_PAYMENT = "AWAITING_PAYMENT"
    PAID = "PAID"
    READY = "READY"
    CANCELED = "CANCELED"
    FINISHED = "FINISHED"

    ORDER_STATUS_CHOICES = (
        (CREATED, "Создан"),
        (IN_PROCESSING, "В обработке"),
        (AWAITING_PAYMENT, "Ожидает оплаты"),
        (PAID, "Оплачен"),
        (READY, "Готов к выдаче"),
        (CANCELED, "Отменен"),
        (FINISHED, "Выдан"),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name="создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="обновлен", auto_now=True)
    status = models.CharField(
        verbose_name="статус",
        choices=ORDER_STATUS_CHOICES,
        max_length=16,
        default=CREATED,
    )
    is_active = models.BooleanField(verbose_name="активен", default=True)

    @property
    def items_with_products(self):
        return self.items.select_related("product")

    def __str__(self):
        return f"Заказ {self.id}"

    def get_total_quantity(self):
        return sum(item.quantity for item in self.items.all())

    def get_total_cost(self):
        return sum(item.cost for item in self.items_with_products)

    def delete(self):
        for item in self.items_with_products:
            Basket.objects.create(
                user=self.user, product=item.product, quantity=item.quantity
            )
        self.is_active = False
        self.save()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name="количество", default=0)

    @property
    def cost(self):
        return self.product.price * self.quantity
