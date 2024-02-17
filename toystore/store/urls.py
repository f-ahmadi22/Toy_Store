from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet, ProductCategoryViewSet, CommentViewSet

category_router = routers.DefaultRouter()
category_router.register('', ProductCategoryViewSet,)

product_router = routers.DefaultRouter()
product_router.register('', ProductViewSet,)

comment_router = routers.DefaultRouter()
comment_router.register('', CommentViewSet,)

urlpatterns = [
    path('categories/', include(category_router.urls)),
    path('products/', include(product_router.urls)),
    path('comments/', include(comment_router.urls)),
]
