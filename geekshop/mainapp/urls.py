from django.urls import path
from . import views


app_name = "mainapp"

urlpatterns = [
    path("", views.products, name="all"),
    path("<int:pk>", views.category, name="category"),
    path("<int:pk>/<int:page>", views.category, name="page_category"),
    path("product/<int:product_id>", views.product, name="product"),
]
