from django.shortcuts import render, get_object_or_404
from mainapp.models import Product, ProductCategory
from adminapp.utils import superuser_required
from django.views.generic import CreateView
from django.utils.decorators import method_decorator
from django.urls import reverse
from adminapp.forms import ProductEditForm
from django.http.response import HttpResponseRedirect


class ProductCreateView(CreateView):
    model = Product
    template_name = "adminapp/product/edit.html"
    fields = "__all__"

    def get_success_url(self):
        return reverse("admin:products", kwargs=self.kwargs)

    @method_decorator(superuser_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        return {"category": self.get_category()}

    def get_category(self):
        return ProductCategory.objects.get(pk=self.kwargs["pk"])

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.get_category()
        return context


@superuser_required
def products(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)
    products = Product.objects.filter(category=category).order_by("id")
    return render(
        request,
        "adminapp/product/products.html",
        context={
            "objects": products,
            "category": category,
            "title": "Продукты",
        },
    )


@superuser_required
def product_read(request, pk):
    title = "продукт/подробнее"
    product = get_object_or_404(Product, pk=pk)
    content = {
        "title": title,
        "object": product,
    }

    return render(request, "adminapp/product/product_read.html", content)


def product_create(request, pk):
    title = "продукт/создание"
    category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == "POST":
        product_form = ProductEditForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse("admin:products", args=[pk]))
    else:
        product_form = ProductEditForm(initial={"category": category})
        content = {"title": title, "update_form": product_form, "category": category}

    return render(request, "adminapp/product/edit.html", content)


@superuser_required
def product_update(request, pk):
    title = "продукт/редактирование"

    edit_product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        edit_form = ProductEditForm(request.POST, request.FILES, instance=edit_product)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(
                reverse("admin:product_update", args=[edit_product.pk])
            )
    else:
        edit_form = ProductEditForm(instance=edit_product)

    content = {
        "title": title,
        "update_form": edit_form,
        "category": edit_product.category,
    }

    return render(request, "adminapp/product/edit.html", content)


@superuser_required
def product_delete(request, pk):
    title = "продукт/удаление"

    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        product.is_active = False
        product.save()
        return HttpResponseRedirect(
            reverse("admin:products", args=[product.category.pk])
        )

    content = {"title": title, "product_to_delete": product}

    return render(request, "adminapp/product/delete.html", content)
