from typing import Any, Dict, Optional
from django.db import models
from django.forms.models import BaseModelForm
from django.shortcuts import redirect, render
from products.models import Products
from django.http import Http404, HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .forms import ProductForm
from django.urls import reverse_lazy
# Create your views here.


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

    def get(self, request, *args, **kwargs):
        '''
            Render product_detail template if the product
            exist, if not render template_name_not_found
        '''
        try:
            return super().get(request, *args, *kwargs)
        except Http404:
            return render(request, self.template_name_not_found)
