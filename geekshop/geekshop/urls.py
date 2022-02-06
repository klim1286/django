from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from mainapp import views as mainapp


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", mainapp.index, name="main"),
    path("contact/", mainapp.contact, name="contact"),
    path("products/", mainapp.products, name="products"),
    path("auth/", include("authapp.urls", namespace="auth")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
