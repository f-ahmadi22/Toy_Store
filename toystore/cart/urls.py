from django.urls import path, include
from rest_framework import routers
from .views import CartProductAPIView

urlpatterns = [
    path('<int:pk>/', CartProductAPIView.as_view(), name='CartProductAPI'),
]
