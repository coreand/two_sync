from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import OrderView

urlpatterns = [
    path('orders/create/', OrderView.as_view()),
    path('auth/', obtain_auth_token),
]
