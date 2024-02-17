from django.db import models
from ..blog.models import MyBaseModel
# Create your models here.


class Category(MyBaseModel):
    title = models.CharField(max_length=250, unique=True, null=False, blank=False, verbose_name="title")
    description = models.TextField(null=False, blank=False, verbose_name="description")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['id']

    def __str__(self):
        return self.title



