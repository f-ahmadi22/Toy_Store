from django.db import models
from django.contrib.auth import get_user_model
from blog.models import MyBaseModel
User = get_user_model()
# Create your models here.


class ProductCategory(MyBaseModel):
    title = models.CharField(max_length=250, unique=True, null=False, blank=False, verbose_name="title")
    description = models.TextField(null=False, blank=False, verbose_name="description")
    thumbnail = models.ImageField(upload_to="media/product/", null=True, blank=True, verbose_name="thumbnail")

    class Meta:
        verbose_name = "ProductCategory"
        verbose_name_plural = "ProductCategories"
        ordering = ['id']

    def __str__(self):
        return self.title


class Product(MyBaseModel):
    title = models.CharField(max_length=250, null=False, blank=False, verbose_name="title")
    description = models.TextField(null=False, blank=False, verbose_name="description")
    category = models.ForeignKey(ProductCategory, related_name="products", on_delete=models.CASCADE,
                                 verbose_name="category")
    thumbnail = models.ImageField(upload_to="media/product/", null=True, blank=True, verbose_name="thumbnail")

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['id']

    def __str__(self):
        return self.title

    def price(self):  # Get last price of the given product
        return self.prices.filter(is_active=True).last()

    def get_images(self):
        # Get images related to the given product
        return ProductMedia.objects.filter(product=self, media_type='image')

    def get_videos(self):
        # Get videos related to the given product
        return ProductMedia.objects.filter(product=self, media_type='video')

    def get_audios(self):
        # Get videos related to the given product
        return ProductMedia.objects.filter(product=self, media_type='audio')

    def get_media(self):
        # Get all media related to the given post
        return ProductMedia.objects.filter(product=self)


class ProductPrice(MyBaseModel):
    product = models.ForeignKey(Product, related_name="prices", on_delete=models.CASCADE, verbose_name="product")
    price = models.FloatField(null=False, blank=False, verbose_name="price")

    class Meta:
        verbose_name = "Price"
        verbose_name_plural = "Prices"
        ordering = ['id']

    def __str__(self):
        return f'{self.product.title} - {self.price}'


class ProductComment(MyBaseModel):
    product = models.ForeignKey(Product, related_name="comments", on_delete=models.CASCADE, verbose_name="product")
    author = models.ForeignKey(User, null=False, blank=False, verbose_name="author", on_delete=models.CASCADE)
    content = models.TextField(null=False, blank=False, verbose_name="content")

    class Meta:
        verbose_name = "ProductComment"
        verbose_name_plural = "ProductComments"
        ordering = ['id']

    def __str__(self):
        return self.product.title


class ProductMedia(MyBaseModel):
    MEDIA_TYPES = [('image', 'image'), ('video', 'video'), ('audio', 'audio')]
    product = models.ForeignKey(Product, related_name='media', on_delete=models.CASCADE, verbose_name="product")
    media_type = models.CharField(max_length=20, choices=MEDIA_TYPES, null=False, blank=False,
                                  verbose_name="media_type")
    media_file = models.FileField(upload_to='media/store/')

    class Meta:
        verbose_name = "ProductMedia"
        verbose_name_plural = "ProductMedia"
        ordering = ['id']

    def __str__(self):
        return self.media_type
