from django.contrib import admin
from django.contrib.admin import register
from .models import Category, Post, Comment, Media
# Register your models here.


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'is_active', 'created_at', 'updated_at')
    list_display_links = ('id', 'title', 'description', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active',)
    list_editable = ('is_active',)
    search_fields = ('title', 'description')


@register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'category', 'is_active', 'created_at', 'updated_at')
    list_display_links = ('id', 'title', 'description', 'category', 'is_active', 'created_at', 'updated_at')
    list_filter = ('category',)
    list_editable = ('is_active',)
    search_fields = ('title', 'description', 'category__title', 'category__description')

