import random
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage
from django.utils import timezone
from .models import Product, ProductCategory

MAIN_MENU_LINKS = [
    {"url": "main", "active": ["main"], "name": "Домой"},
    {
        "url": "products:all",
        "active": ["products:all", "products:category"],
        "name": "Продукты",
    },
    {"url": "contact", "active": ["contact"], "name": "Контакты"},
]


def get_hot_product(queryset):
    return random.choice(queryset)


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
    products = Product.objects.all()
    hot_product = get_hot_product(products)
    return render(
        request,
        "mainapp\products.html",
        context={
            "main_menu_links": MAIN_MENU_LINKS,
            "title": "Продукты",
            "hot_product": hot_product,
            "products": products.exclude(pk=hot_product.pk)[:4],
            "date": timezone.now,
            "catigories": catigories,
        },
    )


def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    catigories = ProductCategory.objects.all()
    return render(
        request,
        "mainapp\product.html",
        context={
            "product": product,
            "category": product.category,
            "main_menu_links": MAIN_MENU_LINKS,
            "title": "Продукты",
            "catigories": catigories,
        },
    )


def category(request, pk, page=1):
    catigories = ProductCategory.objects.all()
    category = get_object_or_404(ProductCategory, pk=pk)
    products = Product.objects.filter(category=category)
    hot_product = get_hot_product(products)
    paginator = Paginator(products.exclude(pk=hot_product.pk), 3)
    try:
        products_page = paginator.page(page)
    except EmptyPage:
        products_page = paginator.page(paginator.num_pages)
    return render(
        request,
        "mainapp\products.html",
        context={
            "main_menu_links": MAIN_MENU_LINKS,
            "title": "Продукты",
            "hot_product": get_hot_product(products),
            "paginator": paginator,
            "page": products_page,
            "products": products_page,            
            "date": timezone.now,
            "catigories": catigories,
            "category" : category,
        },
    )
