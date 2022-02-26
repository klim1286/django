def main_menu_links(request):
    return{
        'main_menu_links': [
            {"url": "main", "active": ["main"], "name": "Домой"},
            {"url": "products:all", "active": ["products:all", "products:category"], "name": "Продукты",},
            {"url": "contact", "active": ["contact"], "name": "Контакты"},
]
    }