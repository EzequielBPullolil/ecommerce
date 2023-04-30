from typing import Any, Dict, Optional
from django.forms.models import BaseModelForm
from django.shortcuts import redirect, render
from products.models import Products
from django.http import Http404, HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .forms import ProductForm
from django.urls import reverse_lazy
# Create your views here.

from products.decorators import handle_not_found


class ProductCreateView(CreateView):
    model = Products
    form_class = ProductForm
    template_name = 'product_create.html'

    def get_object(self):
        id = self.kwargs.get('id')
        return Products.objects.get(id=id)

    def get_success_url(self):
        return reverse_lazy('product_detail', args=[self.object.id])

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        response = super().form_valid(form)
        self.object = form.save()
        return redirect(reverse_lazy('product_detail', args=[self.object.id]))


class ProductDetailView(DetailView):
    model = Products
    template_name = 'product_detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'id'
    template_name_not_found = 'product_not_found.html'

    @handle_not_found
    def get(self, request, *args, **kwargs):
        '''
            Render product_update template if the product
            exist, if not render template_name_not_found
        '''
        return super().get(self, request, *args, **kwargs)


class ProductUpdateView(UpdateView):
    model = Products
    form_class = ProductForm
    template_name = 'product_update.html'
    template_name_not_found = 'product_not_found.html'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse_lazy('product_detail', args=[self.object.id])

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        response = super().form_valid(form)
        self.object = form.save()
        return redirect(reverse_lazy('product_detail', args=[self.object.id]))

    @handle_not_found
    def get(self, request, *args, **kwargs):
        '''
            Render product_update template if the product
            exist, if not render template_name_not_found
        '''
        return super().get(self, request, *args, **kwargs)


class ProductDeleteView(DeleteView):
    model = Products
    template_name = 'product_delete.html'
    template_name_not_found = 'product_not_found.html'
    pk_url_kwarg = 'id'

    @handle_not_found
    def get(self, request, *args, **kwargs):
        '''
            Render product_update template if the product
            exist, if not render template_name_not_found
        '''
        return super().get(self, request, *args, **kwargs)
