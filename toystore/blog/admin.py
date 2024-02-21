from django.contrib import admin
from django.contrib.admin import register
from .models import BlogCategory, Post, BlogComment, BlogMedia
# Register your models here.


class PostInline(admin.StackedInline):  # Post Inline class
    model = Post
    extra = 1  # Just one extra object


@register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):  # Category admin panel customization
    inlines = [PostInline]
    list_display = ('id', 'title', 'description', 'is_active', 'created_at', 'updated_at')
    list_display_links = ('id', 'title', 'description')
    list_filter = ('is_active',)
    list_editable = ('is_active',)
    search_fields = ('title', 'description')


@register(Post)
class PostAdmin(admin.ModelAdmin):  # Post admin panel customization
    list_display = ('id', 'title', 'description', 'category', 'is_active', 'created_at', 'updated_at')
    list_display_links = ('id', 'title', 'description', 'category')
    list_filter = ('category',)
    list_editable = ('is_active',)
    search_fields = ('title', 'description', 'category__title', 'category__description')


@register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):  # Comment admin panel customization
    list_display = ('id', 'post', 'author', 'content', 'is_active', 'created_at', 'updated_at')
    list_display_links = ('id', 'post', 'author', 'content',)
    list_filter = ('post', 'post__category', 'author', 'is_active')
    list_editable = ('is_active', )
    search_fields = ('post__title', 'post__category', 'content', 'author')


@register(BlogMedia)
class BlogMediaAdmin(admin.ModelAdmin):  # Media admin panel customization
    list_display = ('id', 'post', 'media_type', 'media_file', 'is_active', 'created_at', 'updated_at')
    list_display_links = ('id', 'post', 'media_type')
    list_filter = ('media_type', 'is_active',)
    list_editable = ('is_active',)
    search_fields = ('post__title', 'post__category', 'media_type')
