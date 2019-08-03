from django.urls import path
from .views import OrderUpdate

urlpatterns = [
    path('orders/update/', OrderUpdate.as_view({'post': 'update'})),
]
