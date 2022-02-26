from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from authapp.models import ShopUser
from adminapp.utils import superuser_required
from django.utils.decorators import method_decorator
from adminapp.forms import ShopUserCreateAdminForm, ShopUserEditAdminForm
from django.urls import reverse_lazy


class UserCreateView(CreateView):
    model = ShopUser
    template_name = "adminapp/user/edit.html"
    form_class = ShopUserCreateAdminForm
    success_url = reverse_lazy("admin:users")

    @method_decorator(superuser_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex["title"] = "Создание пользователя"
        return super().get_context_data(**kwargs)


class UserListView(ListView):
    model = ShopUser
    template_name = "adminapp/user/users.html"

    @method_decorator(superuser_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex["title"] = "Список пользователей"
        return super().get_context_data(**kwargs)


class UserUpdateView(UpdateView):
    model = ShopUser
    template_name = "adminapp/user/edit.html"
    form_class = ShopUserEditAdminForm
    success_url = reverse_lazy("admin:users")

    @method_decorator(superuser_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex["title"] = "Редактирование пользователя"
        return super().get_context_data(**kwargs)


class UserDeleteView(DeleteView):
    model = ShopUser
    template_name = "adminapp/user/delete.html"
    success_url = reverse_lazy("admin:users")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(success_url)

    @method_decorator(superuser_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex["title"] = "Удаление пользователя"
        return super().get_context_data(**kwargs)
