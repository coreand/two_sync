from django.urls import path
from .views import OrderView

urlpatterns = [
    path('orders/create/', OrderView.as_view()),
]
