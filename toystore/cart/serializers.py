from rest_framework import serializers
from .models import Cart, CartProduct
from authentication.serializers import UserSerializer


class CartSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'total_price']

    def get_total_price(self, obj):
        return obj.get_total_price()



class CartProductSerializer(serializers.ModelSerializer):
    cart = CartSerializer(read_only=True)

    class Meta:
        model = CartProduct
        fields = ['id', 'product', 'price', 'cart']
