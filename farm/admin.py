from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from . models import Farm, FarmManagement, FarmProduct, ProductManagement


@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):
    pass


@admin.register(FarmProduct)
class FarmProductAdmin(admin.ModelAdmin):
    pass


@admin.register(FarmManagement)
class FarmManagementAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductManagement)
class ProductManagementAdmin(admin.ModelAdmin):
    pass
