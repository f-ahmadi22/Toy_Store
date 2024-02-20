from django.contrib import admin
from django.contrib.admin import register
from .models import Cart, CartProduct
# Register your models here.


@register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'is_paid', 'is_active', 'created_at', 'updated_at')
    list_display_links = ('id', 'user', 'is_paid')
    list_filter = ('user', 'is_active')
    list_editable = ('is_active',)
    search_fields = ('user__username',)


@register(CartProduct)
class CartProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'price', 'cart', 'is_active', 'created_at', 'updated_at')
    list_display_links = ('id', 'product', 'price', 'cart')
    list_filter = ('product', 'cart', 'is_active')
    list_editable = ('is_active',)
    search_fields = ('product__title', 'price', 'cart')

