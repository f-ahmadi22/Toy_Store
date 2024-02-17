from django.db import models
from ..blog.models import MyBaseModel, Category
# Create your models here.


class Product(MyBaseModel):
    title = models.CharField(max_length=250, null=False, blank=False, verbose_name="title")
    description = models.TextField(null=False, blank=False, verbose_name="description")
    price = models.IntegerField(null=False, blank=False, verbose_name="price")
    category = models.ForeignKey(Category, related_name="posts", on_delete=models.CASCADE, verbose_name="category")

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['id']

    def __str__(self):
        return self.title
