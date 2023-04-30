from django.urls import path
from .views import (
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView
)
urlpatterns = [
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('<int:id>/', ProductDetailView.as_view(), name='product_detail'),
    path('<int:id>/update', ProductUpdateView.as_view(), name='product_update'),
    path('<int:id>/delete', ProductDeleteView.as_view(), name='product_delete'),

]
