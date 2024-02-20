from django.urls import path, include
from rest_framework import routers
from .views import PayAPIView, PaymentAPIView


urlpatterns = [
    path('payments/', PaymentAPIView.as_view(), name='payments'),
    path('pay/<int:pk>/', PayAPIView.as_view(), name='pay cart'),
]
