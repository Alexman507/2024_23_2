from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from main.forms import ProductForm, VersionForm, VersionFormSet, ProductModeratorForm
from main.models import Product, Contact, Order, Version


class GetContextMixin:
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['version'] = Version.objects.all()
        return context_data


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("main:product_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        return response


class ProductListView(GetContextMixin, ListView):
    model = Product


class ProductDetailView(GetContextMixin, DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['title'] = self.object.name
        return context


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('main:product_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        product_formset = inlineformset_factory(Product, Version, form=VersionForm, formset=VersionFormSet, extra=1)
        if self.request.method == "POST":
            context_data["formset"] = product_formset(self.request.POST, instance=self.object)
        else:
            context_data["formset"] = product_formset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data["formset"]
        if form.is_valid and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if (user.has_perm('main.can_change_product_description') and user.has_perm('main.can_change_product_category')
                and user.has_perm('main.can_change_is_published')):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('main:product_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner or self.request.user.is_superuser:
            return self.object
        raise PermissionDenied


class ContactListView(ListView):
    model = Contact


class OrderCreateView(CreateView):
    model = Order  # Модель
    fields = ('name', 'phone', 'message', 'created_at')  # Поля для заполнения при создании
    success_url = reverse_lazy('main:product_list')  # Адрес для перенаправления после успешного создания

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        return response


class VersionListView(ListView):
    model = Version


class VersionDetailView(DetailView):
    model = Version


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy("main:versions")


class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy("main:versions")


class VersionDeleteView(DeleteView):
    model = Version
    success_url = reverse_lazy("main:versions")
