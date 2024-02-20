from django.urls import path, include
from rest_framework import routers
from .views import PayAPIView, PaymentViewSet

payment_router = routers.DefaultRouter()
payment_router.register('', PaymentViewSet,)

urlpatterns = [
    path('payments/', include(payment_router.urls)),
    path('pay/<int:pk>/', PayAPIView.as_view(), name='pay cart'),
]
