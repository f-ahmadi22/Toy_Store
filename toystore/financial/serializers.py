from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'user', 'cart', 'is_paid']
        read_only_fields = ['user']  # Get user from Token
