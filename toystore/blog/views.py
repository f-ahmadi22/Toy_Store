from django.shortcuts import render
from rest_framework import viewsets, status, filters, permissions, authentication
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post, BlogComment, BlogCategory, BlogMedia
from .serializers import CategorySerializer, PostSerializer, CommentSerializer, MediaSerializer
# Create your views here.


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):  # Get all and detailed category list
    serializer_class = CategorySerializer
    queryset = BlogCategory.objects.filter(is_active=True).order_by('-pk')
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)


class PostViewSet(viewsets.ReadOnlyModelViewSet):  # Get all and detailed post list
    serializer_class = PostSerializer
    queryset = Post.objects.filter(is_active=True).order_by('-pk')
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_fields = ('id', 'category')
    search_fields = ('title', 'description')


class CommentViewSet(viewsets.ModelViewSet):   # Get all and detailed comment list and submit comment
    serializer_class = CommentSerializer
    # IsAuthenticated for submit comment and readonly for get comment list
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = BlogComment.objects.filter(is_active=True).order_by('-pk')
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_fields = ('id', 'post', 'author')
    search_fields = ('author', 'post', 'description')

    # Override the perform_create method to set the current user as the comment author
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


