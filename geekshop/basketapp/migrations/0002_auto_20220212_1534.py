# Generated by Django 3.2.11 on 2022-02-12 12:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0002_alter_product_image"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("basketapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="basket",
            name="product",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="mainapp.product"
            ),
        ),
        migrations.AlterField(
            model_name="basket",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="basket",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
