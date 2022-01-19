from turtle import title
from django.shortcuts import render
from django.utils import timezone

MENU_MAIN_LINKS = [
    {'url': 'main', 'name': 'Домой'},
    {'url': 'products', 'name': 'Продукты'},
    {'url': 'contact', 'name': 'Контакты'},
]
def index(request):
    return render(request, 'mainapp\index.html', context={
        'menu_main_links': MENU_MAIN_LINKS,
        'title': 'Главная',
        'date': timezone.now,
    })


def contact(request):
    return render(request, 'mainapp\contact.html',context={
        'menu_main_links': MENU_MAIN_LINKS,
        'title': 'Контакты',
        'date': timezone.now,
    })


def products(request):
    return render(request, 'mainapp\products.html',context={
        'menu_main_links': MENU_MAIN_LINKS,
        'title': 'Продукты',
        'date': timezone.now,
    })