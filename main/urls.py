from django.urls import path

from .views import (
    dashboard, dash_products, home, register, stores
)


urlpatterns = [
    path('', home, name='home'),
    path('stores/', stores, name='register'),
    path('stores/register/', register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/register/stores/', register, name='register'),
    path('dashboard/products/', dash_products, name='dash-products'),
    path('dashboard/add-product/', register, name='add_product'),
    path('dashboard/requests/', register, name='add_product'),
]
