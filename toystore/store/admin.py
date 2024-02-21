from django.contrib import admin
from django.contrib.admin import register
from .models import ProductCategory, Product, ProductComment, ProductMedia, ProductPrice
# Register your models here.


class ProductInline(admin.StackedInline):
    model = Product
    extra = 1


class PriceInline(admin.StackedInline):
    model = ProductPrice
    extra = 1


@register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    inlines = [ProductInline]
    list_display = ('id', 'title', 'description', 'is_active', 'created_at', 'updated_at')
    list_display_links = ('id', 'title', 'description')
    list_filter = ('is_active',)
    list_editable = ('is_active',)
    search_fields = ('title', 'description')


@register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [PriceInline]
    list_display = ('id', 'title', 'description', 'category', 'price', 'is_active', 'created_at', 'updated_at')
    list_display_links = ('id', 'title', 'description', 'category', 'price')
    list_filter = ('category',)
    list_editable = ('is_active',)
    search_fields = ('title', 'description', 'category__title', 'category__description')


@register(ProductPrice)
class ProductPrice(admin.ModelAdmin):
    list_display = ('id', 'product', 'price', 'is_active', 'created_at', 'updated_at')
    list_display_links = ('id', 'product', 'price')
    list_filter = ('product', 'product__category', 'is_active')
    list_editable = ('is_active',)
    search_fields = ('product__title', 'product__category',)


@register(ProductComment)
class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'author', 'content', 'is_active', 'created_at', 'updated_at')
    list_display_links = ('id', 'product', 'author', 'content',)
    list_filter = ('product', 'product__category', 'author', 'is_active')
    list_editable = ('is_active',)
    search_fields = ('product__title', 'product__category', 'content', 'author')


@register(ProductMedia)
class ProductMediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'media_type', 'media_file', 'is_active', 'created_at', 'updated_at')
    list_display_links = ('id', 'product', 'media_type')
    list_filter = ('media_type', 'is_active',)
    list_editable = ('is_active',)
    search_fields = ('product__title', 'product__category', 'media_type')

