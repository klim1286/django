from turtle import title
from unicodedata import category
from django.shortcuts import render
from django.utils import timezone
from .models import Product, ProductCategory

MAIN_MENU_LINKS = [
    {"url": "main", "name": "Домой"},
    {"url": "products", "name": "Продукты"},
    {"url": "contact", "name": "Контакты"},
]


def index(request):
    products = Product.objects.all()[:4]
    return render(
        request,
        "mainapp\index.html",
        context={
            "main_menu_links": MAIN_MENU_LINKS,
            "title": "Главная",
            "date": timezone.now,
            "products": products,
        },
    )


def contact(request):
    return render(
        request,
        "mainapp\contact.html",
        context={
            "main_menu_links": MAIN_MENU_LINKS,
            "title": "Контакты",
            "date": timezone.now,
        },
    )


def products(request):
    catigories = ProductCategory.objects.all()
    return render(
        request,
        "mainapp\products.html",
        context={
            "main_menu_links": MAIN_MENU_LINKS,
            "title": "Продукты",
            "date": timezone.now,
            "catigories": catigories,
        },
    )
