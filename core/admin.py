from django.contrib import admin

from .models import Pharmacy, Product

@admin.register(Pharmacy)
class PharmacyAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'is_verified')
    list_filter = ('city', 'is_verified')
    search_fields = ('name', 'city')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'pharmacy', 'category', 'price', 'is_available')
    list_filter = ('category', 'is_available', 'pharmacy__city')
    search_fields = ('name', 'category', 'pharmacy__name')
