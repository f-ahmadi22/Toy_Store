from django.db import models
from django.db.models import Sum
from django.contrib.auth import get_user_model
from store.models import Product
from blog.models import MyBaseModel

User = get_user_model()

# Create your models here.


class Cart(MyBaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart', null=False, blank=False,
                             verbose_name='user')

    def __str__(self):
        return f'{self.user} created cart'

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'
        ordering = ['id']

    def get_total_price(self):  # return sum of prices of all products in the cart
        return CartProduct.objects.filter(cart=self.id).aggregate(Sum('price'))

    def get_products(self):  # return all products in the cart
        return CartProduct.objects.filter(cart=self.id)


class CartProduct(MyBaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart', null=False, blank=False,
                                verbose_name='product')
    price = models.FloatField(default=0, blank=False, null=False)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='products', null=False, blank=False,
                             verbose_name='cart')

    def __str__(self):
        return str(self.price)

    class Meta:
        verbose_name = 'CartProduct'
        verbose_name_plural = 'CartProducts'
        ordering = ['id']

