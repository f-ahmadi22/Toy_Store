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


class PaymentAPIView(APIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):

        queryset = Payment.objects.filter(is_paid=True,user=request.user).order_by('-pk')
        serializer = PaymentSerializer(queryset, many=True)
        return Response(serializer.data)


class PayAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        cart = Cart.objects.get(pk=pk)
        if cart.is_active:
            return Response(f'{request.user} paid this before')
        else:

            cart.is_active = False

            payment = Payment.objects.create(cart=cart, user=request.user, is_paid=True)
            payment.save()
            return Response(f'{request.user} paid {cart.get_total_price()}, is_paid = True')
