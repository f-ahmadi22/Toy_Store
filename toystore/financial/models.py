from django.db import models
from blog.models import MyBaseModel
from cart.models import Cart
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()


class Payment(MyBaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='payments', null=False, blank=False,
                             verbose_name='cart')
    is_paid = models.BooleanField(default=False, verbose_name='is paid')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments', null=False, blank=False,
                             verbose_name='user')

    def __str__(self):
        return self.cart

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
        ordering = ['id']

