from rest_framework import viewsets
from rest_framework.response import Response

from .models import Order
from .serializers import OrderSerializer


class OrderUpdate(viewsets.ViewSet):
    def update(self, request, **kwargs):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        order_number = serializer.validated_data['order_number']
        status = serializer.validated_data['status']
        Order.objects.filter(order_number=order_number).update(status=status)

        return Response({'status': 'ok'})
