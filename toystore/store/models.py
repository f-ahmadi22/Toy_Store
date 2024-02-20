from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
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
    category = models.ForeignKey(ProductCategory, related_name="posts", on_delete=models.CASCADE,
                                 verbose_name="category")

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['id']

    def __str__(self):
        return self.title

    @property
    def price(self):
        return self.prices.filter(is_active=True).last()


class ProductPrice(BaseModel):
    product = models.ForeignKey(Product, related_name="prices", on_delete=models.CASCADE, verbose_name="product")
    price = models.DecimalField()

    class Meta:
        verbose_name = "Price"
        verbose_name_plural = "Prices"
        ordering = ['id']

    def __str__(self):
        return f'{self.product.title} - {self.price}'


class ProductComment(BaseModel):
    product = models.ForeignKey(Product, related_name="comments", on_delete=models.CASCADE, verbose_name="product")
    author = models.ForeignKey(User, null=False, blank=False, verbose_name="author", on_delete=models.CASCADE)
    content = models.TextField(null=False, blank=False, verbose_name="content")

    class Meta:
        verbose_name = "ProductComment"
        verbose_name_plural = "ProductComments"
        ordering = ['id']

    def __str__(self):
        return self.author


class ProductMedia(BaseModel):
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

    @property
    def get_images(self):
        """
        Get images related to the given post.
        """
        return ProductMedia.objects.filter(product=self.product, media_type='image')

    @property
    def get_videos(self):
        """
        Get videos related to the given post.
        """
        return ProductMedia.objects.filter(product=self.product, media_type='video')

    @property
    def get_audios(self):
        """
        Get audios related to the given post.
        """
        return ProductMedia.objects.filter(product=self.product, media_type='audio')
