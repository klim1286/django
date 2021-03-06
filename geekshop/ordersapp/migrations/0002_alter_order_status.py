# Generated by Django 3.2.12 on 2022-02-27 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ordersapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("CREATED", "Создан"),
                    ("IN_PROCESSING", "В обработке"),
                    ("AWAITING_PAYMENT", "Ожидает оплаты"),
                    ("PAID", "Оплачен"),
                    ("READY", "Готов к выдаче"),
                    ("CANCELED", "Отменен"),
                    ("FINISHED", "Выдан"),
                ],
                default="CREATED",
                max_length=16,
                verbose_name="статус",
            ),
        ),
    ]
