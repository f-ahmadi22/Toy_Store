from rest_framework import serializers
from .models import Payment
from cart.serializers import CartSerializer
from authentication.serializers import UserSerializer


class PaymentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    cart = CartSerializer(read_only=True)

    class Meta:
        model = Payment
        fields = ['id', 'user', 'cart', 'is_paid']
        read_only_fields = ['user']  # Get user from Token
