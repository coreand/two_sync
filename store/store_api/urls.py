from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import OrderUpdate

urlpatterns = [
    path('orders/update/', OrderUpdate.as_view({'post': 'update'})),
    path('auth/', obtain_auth_token),
]
