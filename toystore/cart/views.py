from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets, permissions, authentication
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Cart, CartProduct
from .serializers import CartProductSerializer
from store.models import Product


class CartProductAPIView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        # Get the product instance
        product = get_object_or_404(Product, id=pk)

        # Get the user (assuming it's authenticated)
        user = request.user

        # Check if the user has an active cart
        cart = Cart.objects.filter(user=user, is_active=True).first()

        # If user doesn't have an active cart, create a new one
        if not cart:
            cart = Cart.objects.create(user=user, is_active=True)

        # If product doesn't exist in the cart, create a new CartProduct
        new_cart_product = CartProduct.objects.create(product=product, price=product.price().price, cart=cart,
                                                      is_active=True)
        serializer = CartProductSerializer(new_cart_product)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
