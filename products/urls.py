from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='product-list'),
    path('product/<str:pk>/', views.product_detail, name='product-detail'),
]
