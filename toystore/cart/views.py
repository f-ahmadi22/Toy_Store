from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Cart, CartProduct
from .serializers import CartProductSerializer

class CartProductAPIView(APIView):
    def post(self, request, product_id):
        # Get the product instance
        product = get_object_or_404(Product, id=product_id)

        # Get the user (assuming it's authenticated)
        user = request.user

        # Check if the user has an active cart
        cart = Cart.objects.filter(user=user, is_active=True).first()

        # If user doesn't have an active cart, create a new one
        if not cart:
            cart = Cart.objects.create(user=user, is_active=True)

        # Check if the product is already in the cart
        existing_cart_product = CartProduct.objects.filter(cart=cart, product=product).first()

        # If product already exists in the cart, increment its quantity
        if existing_cart_product:
            existing_cart_product.quantity += 1
            existing_cart_product.save()
            serializer = CartProductSerializer(existing_cart_product)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # If product doesn't exist in the cart, create a new CartProduct
        new_cart_product = CartProduct.objects.create(product=product, price=product.price, cart=cart)
        serializer = CartProductSerializer(new_cart_product)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
