from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets, status, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product, ProductComment, ProductCategory, ProductMedia
from .serializers import CategorySerializer, ProductSerializer, CommentSerializer, MediaSerializer
# Create your views here.


class ProductCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = ProductCategory.objects.filter(is_active=True).order_by('-pk')
    # permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Product.objects.filter(is_active=True).order_by('-pk')
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_fields = ('id', 'category')
    search_fields = ('title', 'description')


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    # permission_classes = [permissions.IsAuthenticated]
    queryset = ProductComment.objects.filter(is_active=True).order_by('-pk')
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_fields = ('id', 'product', 'author')
    search_fields = ('author', 'product', 'description')


