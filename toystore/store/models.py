from django.db import models
# Create your models here.


class BaseModel(models.Model):
    is_active = models.BooleanField(default=False, verbose_name='Is active')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    class Meta:
        abstract = True
        ordering = ['pk']


class ProductCategory(BaseModel):
    title = models.CharField(max_length=250, unique=True, null=False, blank=False, verbose_name="title")
    description = models.TextField(null=False, blank=False, verbose_name="description")

    class Meta:
        verbose_name = "ProductCategory"
        verbose_name_plural = "ProductCategories"
        ordering = ['id']

    def __str__(self):
        return self.title


class Product(BaseModel):
    title = models.CharField(max_length=250, null=False, blank=False, verbose_name="title")
    description = models.TextField(null=False, blank=False, verbose_name="description")
    price = models.IntegerField(null=False, blank=False, verbose_name="price")
    category = models.ForeignKey(ProductCategory, related_name="posts", on_delete=models.CASCADE, verbose_name="category")

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['id']

    def __str__(self):
        return self.title
