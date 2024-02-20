from django.db import models
from blog.models import MyBaseModel
from cart.models import Cart
# Create your models here.


class Payment(MyBaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='payments', null=False, blank=False,
                             verbose_name='cart')
    is_paid = models.BooleanField(default=False, verbose_name='is paid')

    def __str__(self):
        return self.cart

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
        ordering = ['id']

