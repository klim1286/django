from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Product, ProductCategory

MAIN_MENU_LINKS = [
    {"url": "main", "active":["main"], "name": "Домой"},
    {"url": "products:all","active":["products:all", "products:category"], "name": "Продукты"},
    {"url": "contact", "active":["contact"], "name": "Контакты"},
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
    products = Product.objects.all()[:4]
    return render(
        request,
        "mainapp\products.html",
        context={
            "main_menu_links": MAIN_MENU_LINKS,
            "title": "Продукты",
            "products": products,
            "date": timezone.now,
            "catigories": catigories,
        },
    )


def category(request, pk):
    catigories = ProductCategory.objects.all()
    category = get_object_or_404(ProductCategory, pk=pk)
    #category = ProductCategory.objects.get(pk=pk)
    products = Product.objects.filter(category=category)
    return render(
        request,
        "mainapp\products.html",
        context={
            "main_menu_links": MAIN_MENU_LINKS,
            "title": "Продукты",
            "products": products,
            "date": timezone.now,
            "catigories": catigories,
        },
    )