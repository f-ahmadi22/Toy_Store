from typing import Tuple

from django.shortcuts import render
from rest_framework import viewsets, status, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post, Comment, Category, Media
from .serializers import CategorySerializer, PostSerializer, CommentSerializer, MediaSerializer
# Create your views here.


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(is_active=True).order_by('-pk')
    # permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.filter(is_active=True).order_by('-pk')
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_fields = ('id', 'category')
    search_fields = ('title', 'description')


class CommentViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CommentSerializer
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Comment.objects.filter(is_active=True).order_by('-pk')
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_fields = ('id', 'post', 'author')
    search_fields = ('author', 'post', 'description')


