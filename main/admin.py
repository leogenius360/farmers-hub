from django.contrib import admin

from . models import Product, Sale, Store


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = (
        'date_created', 'name', 'owner'
    )
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'store', 'name', 'in_stock', 'sales_price', 'qty_sold',
        'credit_sales', 'paid_sales'
    )
    pass


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    pass
