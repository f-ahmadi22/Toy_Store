from django.db import models
from django.db.models import Sum
from django.contrib.auth import get_user_model
from store.models import Product
from blog.models import MyBaseModel

User = get_user_model()

# Create your models here.


class CartBaseModel(models.Model):
    is_active = models.BooleanField(default=False, verbose_name='Is active')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    class Meta:
        abstract = True
        ordering = ['pk']


class Cart(MyBaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart', null=False, blank=False,
                             verbose_name='user')
    is_paid = models.BooleanField(default=False, verbose_name='Is paid')

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'
        ordering = ['id']

    def get_total_price(self):
        return CartProduct.objects.filter(cart=self.id).aggregate(price=Sum('price'))['price__sum']

    def get_products(self):
        return CartProduct.objects.filter(cart=self.id)


class CartProduct(MyBaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart', null=False, blank=False,
                                verbose_name='product')
    price = models.FloatField(default=0, blank=False, null=False)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='products', null=False, blank=False,
                             verbose_name='cart')

    def __str__(self):
        return self.product

    class Meta:
        verbose_name = 'CartProduct'
        verbose_name_plural = 'CartProducts'
        ordering = ['id']

