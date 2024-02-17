from django.contrib import admin
from django.contrib.admin import register
from .models import Category, Post, Comment, Media
# Register your models here.


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'is_active', 'created_at', 'updated_at')
    list_display_links = ('id', 'title', 'description')
    list_filter = ('is_active',)
    list_editable = ('is_active',)
    search_fields = ('title', 'description')


@register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'category', 'is_active', 'created_at', 'updated_at')
    list_display_links = ('id', 'title', 'description', 'category')
    list_filter = ('category',)
    list_editable = ('is_active',)
    search_fields = ('title', 'description', 'category__title', 'category__description')


@register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'author', 'content', 'is_approved', 'is_active', 'created_at', 'updated_at')
    list_display_links = ('id', 'post', 'author', 'content',)
    list_filter = ('post', 'post__category', 'author', 'is_approved', 'is_active')
    list_editable = ('is_active', 'is_approved')
    search_fields = ('post__title', 'post__category', 'content', 'author')


@register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'media_type', 'media_file', 'is_active', 'created_at', 'updated_at')
    list_display_links = ('id', 'post', 'media_type')
    list_filter = ('media_type', 'is_active',)
    list_editable = ('is_active',)
    search_fields = ('post__title', 'post__category', 'media_type')

