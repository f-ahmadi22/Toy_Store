from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=250, unique=True, null=False, blank=False, verbose_name="title")
    description = models.TextField(null=False, blank=False, verbose_name="description")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['id']

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=250, null=False, blank=False, verbose_name="title")
    description = models.TextField(null=False, blank=False, verbose_name="description")
    category = models.ForeignKey(Category, related_name="posts", on_delete=models.CASCADE, verbose_name="category")

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['id']

    def __str__(self):
        return self.title
