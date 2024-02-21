from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets, status, filters, permissions, authentication
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product, ProductComment, ProductCategory, ProductMedia
from .serializers import CategorySerializer, ProductSerializer, CommentSerializer, MediaSerializer
# Create your views here.


class ProductCategoryViewSet(viewsets.ReadOnlyModelViewSet):  # Get all and detailed category list
    serializer_class = CategorySerializer
    queryset = ProductCategory.objects.filter(is_active=True).order_by('-pk')
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)


class ProductViewSet(viewsets.ReadOnlyModelViewSet):  # Get all and detailed product list
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(is_active=True).order_by('-pk')
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_fields = ('id', 'category')
    search_fields = ('title', 'description')


class CommentViewSet(viewsets.ModelViewSet):  # Get all and detailed comment list and submit comment
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = ProductComment.objects.filter(is_active=True).order_by('-pk')
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_fields = ('id', 'product', 'author')
    search_fields = ('author', 'product', 'description')

    # Override the perform_create method to set the current user as the comment author
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


