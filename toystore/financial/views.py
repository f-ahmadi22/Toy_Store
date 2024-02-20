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


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.filter(is_paid=True).order_by('-pk')
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)


class PayAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def post(self, request, pk):
        cart = Cart.objects.get(pk=pk)
        cart.is_active = False

        payment = Payment.objects.create(cart=cart, user=request.user, is_paid=True)
        payment.save()

        return Response(f'{request.user} paid {cart.get_total_price()}, is_paid = True')
