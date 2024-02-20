from django.contrib import admin
from django.contrib.admin import register
from .models import Payment
# Register your models here.


@register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'is_paid', 'is_active', 'created_at', 'updated_at')
    list_display_links = ('id', 'cart', 'is_paid')
    list_filter = ('cart', 'is_paid', 'is_active')
    list_editable = ('is_active',)
    search_fields = ('cart', 'cart__user')
