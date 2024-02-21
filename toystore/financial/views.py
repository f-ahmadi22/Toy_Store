from django.shortcuts import render
from rest_framework import viewsets, filters, authentication, permissions
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Payment
from cart.models import Cart
from .serializers import PaymentSerializer
# Create your views here.


class PaymentAPIView(APIView):  # Get all payments
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):

        queryset = Payment.objects.filter(is_paid=True,user=request.user).order_by('-pk')
        serializer = PaymentSerializer(queryset, many=True)
        return Response(serializer.data)


class PayAPIView(APIView):  # Pay cart that it's id is passed in request query params
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        cart = Cart.objects.get(pk=pk)  # get cart by pk
        user = request.user
        if cart.is_active:
            return Response(f'{user} paid this before')
        else:
            cart.is_active = True
            payment = Payment.objects.create(cart=cart, user=user, is_paid=True)
            payment.save()
            return Response(f'{user} paid {cart.get_total_price()}, is_paid = True')
