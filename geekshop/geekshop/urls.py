from django.conf import settings
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from mainapp import views as mainapp


urlpatterns = [
    # path("admins/", admin.site.urls),
    path("admin/", include("adminapp.urls", namespace="admin")),
    path("", mainapp.index, name="main"),
    path("contact/", mainapp.contact, name="contact"),
    path("products/", include("mainapp.urls", namespace="products")),
    path("auth/", include("authapp.urls", namespace="auth")),
    path("basket/", include("basketapp.urls", namespace="basket")),
    path("", include("social_django.urls", namespace="social")),
    path("orders/", include("ordersapp.urls", namespace="orders")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
