from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from authapp.models import ShopUser
from adminapp.utils import superuser_required
from adminapp.forms import ShopUserAdminForm
from django.urls import reverse
from django.shortcuts import render, get_object_or_404


@superuser_required
def user_create(request):
    if request.method == "POST":
        form = ShopUserAdminForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("admin:users"))
    else:
        form = ShopUserAdminForm()

    return render(
        request,
        "adminapp/user/edit.html",
        context={
            "title": "Создание пользователя",
            "form": form,
        },
    )


@superuser_required
def users(request):
    users = ShopUser.objects.all().order_by("id")
    return render(
        request,
        "adminapp/user/users.html",
        context={
            "objects": users,
            "title": "Пользователи",
        },
    )


@superuser_required
def user_update(request, pk):
    user = get_object_or_404(ShopUser, pk)
    if request.method == "POST":
        form = ShopUserAdminForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("admin:users"))
    else:
        form = ShopUserAdminForm(instance=user)

    return render(
        request,
        "adminapp/user/edit.html",
        context={
            "title": "Редактирование пользователя",
            "form": form,
        },
    )


@superuser_required
def user_delete(request, pk):
    title = "пользователи/удаление"

    user = get_object_or_404(ShopUser, pk=pk)

    if request.method == "POST":
        # user.delete()
        # вместо удаления лучше сделаем неактивным
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse("admin:users"))

    content = {"title": title, "user_to_delete": user}

    return render(request, "adminapp/user/delete.html", content)
